#!/usr/bin/env python3
"""Validate the public Ranger Foundry repository with the Python standard library."""

from __future__ import annotations

import ast
import json
import os
from pathlib import Path
import re
import stat
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "ranger-foundry"
PLUGIN_DIR = ROOT / "plugins" / PLUGIN_NAME
REPOSITORY_URL = "https://github.com/darkrangerstudios/ranger-foundry"

EXPECTED_SKILLS = (
    "ranger-agent-instructions",
    "ranger-assembly-line",
    "ranger-cause-analysis",
    "ranger-handoff",
    "ranger-kestrel-review",
    "ranger-plan-assurance",
    "ranger-prototype",
    "ranger-questionnaire",
    "ranger-slice-plan",
)

EXPECTED_IMPLICIT_POLICY = {skill_name: True for skill_name in EXPECTED_SKILLS}
EXPLICIT_ONLY_SKILLS = {
    skill_name for skill_name, allowed in EXPECTED_IMPLICIT_POLICY.items() if not allowed
}
ASSEMBLY_LINE_SKILL = "ranger-assembly-line"
ASSEMBLY_LINE_SPECIALISTS = set(EXPECTED_SKILLS) - {ASSEMBLY_LINE_SKILL}

ROOT_FILES = {
    Path(".agents/plugins/marketplace.json"),
    Path(".github/workflows/ci.yml"),
    Path(".gitignore"),
    Path("CHANGELOG.md"),
    Path("CONTRIBUTING.md"),
    Path("LICENSE"),
    Path("README.md"),
    Path("SECURITY.md"),
    Path("docs/commissioning.md"),
    Path("docs/dispatch-policy.md"),
    Path("docs/platform-adapters.md"),
    Path("docs/skill-review.md"),
    Path("evals/routing-cases.json"),
    Path("plugins/ranger-foundry/.codex-plugin/plugin.json"),
    Path("scripts/validate.py"),
}

SKILL_FILES = {
    Path("plugins/ranger-foundry/skills") / name / relative
    for name in EXPECTED_SKILLS
    for relative in (Path("SKILL.md"), Path("agents/openai.yaml"))
}

ALLOWED_FILES = ROOT_FILES | SKILL_FILES
IGNORED_NAMES = {".git", ".DS_Store", "__pycache__", ".pytest_cache"}

BLOCKED_COMPONENTS = {
    ".app.json",
    ".mcp.json",
    "hooks",
    "install",
    "installer",
    "node_modules",
    "package-lock.json",
    "package.json",
    "requirements.txt",
    "setup.py",
}

NETWORK_MODULES = {
    "ftplib",
    "http",
    "socket",
    "smtplib",
    "subprocess",
    "urllib",
}

ALLOWED_PYTHON_MODULES = {
    "__future__",
    "ast",
    "json",
    "os",
    "pathlib",
    "re",
    "stat",
    "sys",
    "typing",
}


def joined(*parts: str) -> str:
    return "".join(parts)


FORBIDDEN_PATTERNS = (
    (
        "email address",
        re.compile(r"(?i)(?<![\w.+-])[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}(?![\w.-])"),
    ),
    (
        "private home path",
        re.compile(
            joined(
                r"(?i)(?:/us",
                r"ers/[a-z0-9._-]+|/home/[a-z0-9._-]+|c:\\us",
                r"ers\\[^\\\s]+|/private/(?:tmp|var)/|~/(?:\.|[a-z0-9]))",
            )
        ),
    ),
    (
        "local file URI",
        re.compile(joined(r"(?i)fi", r"le://")),
    ),
    (
        "IP address",
        re.compile(
            r"(?<![\w.])(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}(?![\w.])"
        ),
    ),
    (
        "private key marker",
        re.compile(joined("-----BE", "GIN ", "PRIVATE ", "KEY-----")),
    ),
    (
        "credential-like token",
        re.compile(
            joined(
                r"(?i)(?:\bsk-[a-z0-9_-]{16,}|\bghp_[a-z0-9]{20,}|",
                r"\bgithub_pat_[a-z0-9_]{20,}|\bAIza[a-z0-9_-]{20,}|",
                r"\beyJ[a-z0-9_-]{10,}\.[a-z0-9_-]{10,}\.[a-z0-9_-]{10,})",
            )
        ),
    ),
    (
        "assigned credential",
        re.compile(
            r"(?i)\b(?:api[_ -]?key|access[_ -]?token|client[_ -]?secret|service[_ -]?key)\s*[:=]\s*['\"]?[a-z0-9_./+-]{12,}"
        ),
    ),
    (
        "environment identifier",
        re.compile(
            r"(?i)\b(?:project[_ -]?(?:id|ref)|machine[_ -]?id|hostname)\s*[:=]\s*['\"]?[a-z0-9_.-]{4,}"
        ),
    ),
    (
        "source attribution claim",
        re.compile(r"(?i)\b(?:adapted|copied|derived|inspired)\s+from\b"),
    ),
)

URL_PATTERN = re.compile(r"https?://[^\s)>\]}'\"]+")
SEMVER_PATTERN = re.compile(
    r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?"
)
SKILL_NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
CASE_ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

CASE_KINDS = {
    "authority-boundary",
    "collision",
    "direct",
    "indirect",
    "negative",
}

FORBIDDEN_ACTIONS = {
    "commit-or-push",
    "contact-recipient",
    "deploy-or-publish",
    "edit-files",
    "implement-fix",
    "persist-sensitive-data",
    "rotate-credentials",
    "run-destructive-step",
    "self-attest-independent-review",
    "send-message",
    "update-external-tracker",
}


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def repository_paths(errors: list[str]) -> list[Path]:
    paths: list[Path] = []
    for current, directories, files in os.walk(ROOT, followlinks=False):
        current_path = Path(current)
        rel_current = current_path.relative_to(ROOT)

        if rel_current.parts and rel_current.parts[0] == ".git":
            directories[:] = []
            continue

        retained_directories: list[str] = []
        for name in sorted(directories):
            path = current_path / name
            if name in IGNORED_NAMES:
                continue
            if path.is_symlink():
                add_error(errors, f"symbolic link is not allowed: {relative(path)}")
                continue
            retained_directories.append(name)
        directories[:] = retained_directories

        for name in sorted(files):
            if name in IGNORED_NAMES:
                continue
            path = current_path / name
            if path.is_symlink():
                add_error(errors, f"symbolic link is not allowed: {relative(path)}")
                continue
            paths.append(path)

    return sorted(paths)


def read_text(path: Path, errors: list[str]) -> str | None:
    try:
        data = path.read_bytes()
    except OSError as exc:
        add_error(errors, f"cannot read {relative(path)}: {exc}")
        return None

    if b"\x00" in data:
        add_error(errors, f"binary content is not allowed: {relative(path)}")
        return None

    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        add_error(errors, f"file is not valid UTF-8: {relative(path)}")
        return None


def check_file_allowlist(paths: list[Path], errors: list[str]) -> None:
    actual = {path.relative_to(ROOT) for path in paths}

    for missing in sorted(ALLOWED_FILES - actual):
        add_error(errors, f"required file is missing: {missing.as_posix()}")

    for unexpected in sorted(actual - ALLOWED_FILES):
        add_error(errors, f"file is outside the public allowlist: {unexpected.as_posix()}")

    for path in paths:
        rel = path.relative_to(ROOT)
        if any(part.casefold() in BLOCKED_COMPONENTS for part in rel.parts):
            add_error(errors, f"blocked component is present: {rel.as_posix()}")
        try:
            mode = path.stat().st_mode
        except OSError as exc:
            add_error(errors, f"cannot inspect {rel.as_posix()}: {exc}")
            continue
        if mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH):
            add_error(errors, f"executable file is not allowed: {rel.as_posix()}")


def check_public_text(path: Path, text: str, errors: list[str]) -> None:
    rel = relative(path)
    for label, pattern in FORBIDDEN_PATTERNS:
        match = pattern.search(text)
        if match:
            line = text.count("\n", 0, match.start()) + 1
            add_error(errors, f"{rel}:{line}: contains {label}")

    for match in URL_PATTERN.finditer(text):
        url = match.group(0).rstrip(".,;:")
        if not (url == REPOSITORY_URL or url.startswith(REPOSITORY_URL + "/")):
            line = text.count("\n", 0, match.start()) + 1
            add_error(errors, f"{rel}:{line}: URL is outside the repository allowlist: {url}")


def load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    text = read_text(path, errors)
    if text is None:
        return None
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        add_error(errors, f"invalid JSON in {relative(path)}: {exc}")
        return None
    if not isinstance(value, dict):
        add_error(errors, f"JSON root must be an object: {relative(path)}")
        return None
    return value


def require_equal(
    value: Any,
    expected: Any,
    label: str,
    errors: list[str],
) -> None:
    if value != expected:
        add_error(errors, f"{label} must be {expected!r}; found {value!r}")


def check_plugin_manifest(errors: list[str]) -> None:
    path = PLUGIN_DIR / ".codex-plugin" / "plugin.json"
    manifest = load_json(path, errors)
    if manifest is None:
        return

    required_keys = {
        "name",
        "version",
        "description",
        "author",
        "homepage",
        "repository",
        "license",
        "keywords",
        "skills",
        "interface",
    }
    if set(manifest) != required_keys:
        add_error(
            errors,
            "plugin manifest keys must be exactly: " + ", ".join(sorted(required_keys)),
        )

    require_equal(manifest.get("name"), PLUGIN_NAME, "plugin name", errors)
    require_equal(manifest.get("homepage"), REPOSITORY_URL, "plugin homepage", errors)
    require_equal(manifest.get("repository"), REPOSITORY_URL, "plugin repository", errors)
    require_equal(manifest.get("license"), "MIT", "plugin license", errors)
    require_equal(manifest.get("skills"), "./skills/", "plugin skills path", errors)

    version = manifest.get("version")
    if not isinstance(version, str) or SEMVER_PATTERN.fullmatch(version) is None:
        add_error(errors, f"plugin version must be strict semantic versioning; found {version!r}")

    description = manifest.get("description")
    if not isinstance(description, str) or not 20 <= len(description) <= 160:
        add_error(errors, "plugin description must contain 20 to 160 characters")

    require_equal(
        manifest.get("author"),
        {"name": "Dark Ranger Studios", "url": REPOSITORY_URL},
        "plugin author",
        errors,
    )

    keywords = manifest.get("keywords")
    if not isinstance(keywords, list) or not keywords or not all(
        isinstance(item, str) and item for item in keywords
    ):
        add_error(errors, "plugin keywords must be a non-empty list of strings")

    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        add_error(errors, "plugin interface must be an object")
        return

    interface_keys = {
        "displayName",
        "shortDescription",
        "longDescription",
        "developerName",
        "category",
        "capabilities",
        "defaultPrompt",
    }
    if set(interface) != interface_keys:
        add_error(
            errors,
            "plugin interface keys must be exactly: " + ", ".join(sorted(interface_keys)),
        )

    require_equal(interface.get("displayName"), "Ranger Foundry", "display name", errors)
    require_equal(interface.get("developerName"), "Dark Ranger Studios", "developer name", errors)
    require_equal(interface.get("category"), "Productivity", "plugin category", errors)
    require_equal(interface.get("capabilities"), ["Interactive"], "plugin capabilities", errors)

    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        add_error(errors, "plugin defaultPrompt must contain one to three prompts")
    elif not all(isinstance(prompt, str) and 1 <= len(prompt) <= 128 for prompt in prompts):
        add_error(errors, "each plugin default prompt must contain 1 to 128 characters")


def check_marketplace(errors: list[str]) -> None:
    path = ROOT / ".agents" / "plugins" / "marketplace.json"
    marketplace = load_json(path, errors)
    if marketplace is None:
        return

    if set(marketplace) != {"name", "interface", "plugins"}:
        add_error(errors, "marketplace keys must be exactly: interface, name, plugins")
    require_equal(marketplace.get("name"), PLUGIN_NAME, "marketplace name", errors)
    require_equal(
        marketplace.get("interface"),
        {"displayName": "Ranger Foundry"},
        "marketplace interface",
        errors,
    )

    expected_plugin = {
        "name": PLUGIN_NAME,
        "source": {"source": "local", "path": "./plugins/ranger-foundry"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }
    require_equal(marketplace.get("plugins"), [expected_plugin], "marketplace plugins", errors)


def check_routing_cases(errors: list[str]) -> None:
    path = ROOT / "evals" / "routing-cases.json"
    suite = load_json(path, errors)
    if suite is None:
        return

    expected_suite_keys = {"schema_version", "evaluation_mode", "cases"}
    if set(suite) != expected_suite_keys:
        add_error(
            errors,
            "routing corpus keys must be exactly: cases, evaluation_mode, schema_version",
        )
    require_equal(suite.get("schema_version"), 2, "routing schema version", errors)
    require_equal(
        suite.get("evaluation_mode"),
        "declarative-expectations-only",
        "routing evaluation mode",
        errors,
    )

    cases = suite.get("cases")
    if not isinstance(cases, list) or not cases:
        add_error(errors, "routing cases must be a non-empty list")
        return

    expected_case_keys = {
        "id",
        "kind",
        "prompt",
        "expected_skill",
        "excluded_skills",
        "forbidden_actions",
    }
    valid_skills = set(EXPECTED_SKILLS)
    seen_ids: set[str] = set()
    seen_prompts: set[str] = set()
    seen_kinds: set[str] = set()
    coverage: dict[str, set[str]] = {
        "direct": set(),
        "indirect": set(),
        "authority-boundary": set(),
    }
    assembly_collision_coverage: set[str] = set()

    for index, case in enumerate(cases):
        label = f"routing case {index + 1}"
        if not isinstance(case, dict):
            add_error(errors, f"{label} must be an object")
            continue
        if set(case) != expected_case_keys:
            add_error(errors, f"{label} must contain exactly: " + ", ".join(sorted(expected_case_keys)))

        case_id = case.get("id")
        kind = case.get("kind")
        prompt = case.get("prompt")
        expected_skill = case.get("expected_skill")
        excluded_skills = case.get("excluded_skills")
        forbidden_actions = case.get("forbidden_actions")

        if not isinstance(case_id, str) or CASE_ID_PATTERN.fullmatch(case_id) is None:
            add_error(errors, f"{label} has an invalid id: {case_id!r}")
        elif case_id in seen_ids:
            add_error(errors, f"duplicate routing case id: {case_id}")
        else:
            seen_ids.add(case_id)

        if kind not in CASE_KINDS:
            add_error(errors, f"{label} has an invalid kind: {kind!r}")
        else:
            seen_kinds.add(kind)
            if isinstance(case_id, str) and not case_id.startswith(kind + "-"):
                add_error(errors, f"{case_id} must begin with its kind")

        if not isinstance(prompt, str) or not 20 <= len(prompt) <= 500 or prompt != prompt.strip():
            add_error(errors, f"{label} prompt must be trimmed and contain 20 to 500 characters")
        elif "\n" in prompt:
            add_error(errors, f"{label} prompt must be a single line")
        else:
            if prompt in seen_prompts:
                add_error(errors, f"duplicate routing prompt in {case_id}")
            seen_prompts.add(prompt)
            if URL_PATTERN.search(prompt):
                add_error(errors, f"{case_id} prompt must be synthetic and contain no URL")

        if expected_skill is not None and expected_skill not in valid_skills:
            add_error(errors, f"{label} has an invalid expected_skill: {expected_skill!r}")

        if not isinstance(excluded_skills, list) or not all(
            isinstance(skill, str) and skill in valid_skills for skill in excluded_skills
        ):
            add_error(errors, f"{label} excluded_skills must contain only known skills")
            excluded_skills = []
        elif len(excluded_skills) != len(set(excluded_skills)):
            add_error(errors, f"{label} excluded_skills contains a duplicate")

        if expected_skill in excluded_skills:
            add_error(errors, f"{label} cannot exclude its expected skill")

        if not isinstance(forbidden_actions, list) or not all(
            isinstance(action, str) and action in FORBIDDEN_ACTIONS
            for action in forbidden_actions
        ):
            add_error(errors, f"{label} forbidden_actions contains an unknown action")
            forbidden_actions = []
        elif len(forbidden_actions) != len(set(forbidden_actions)):
            add_error(errors, f"{label} forbidden_actions contains a duplicate")

        if kind == "negative":
            if expected_skill is not None:
                add_error(errors, f"{label} negative case must expect null")
            if not excluded_skills:
                add_error(errors, f"{label} negative case must name at least one excluded skill")
        elif kind == "indirect" and expected_skill is None:
            if not excluded_skills or not set(excluded_skills).issubset(EXPLICIT_ONLY_SKILLS):
                add_error(
                    errors,
                    f"{label} null indirect case must exclude only explicit-only skills",
                )
        elif kind in CASE_KINDS and expected_skill is None:
            add_error(errors, f"{label} {kind} case must expect a skill")

        if kind == "collision" and not excluded_skills:
            add_error(errors, f"{label} collision case must name a competing skill")
        elif (
            kind == "collision"
            and isinstance(expected_skill, str)
            and expected_skill in ASSEMBLY_LINE_SPECIALISTS
            and ASSEMBLY_LINE_SKILL in excluded_skills
        ):
            assembly_collision_coverage.add(expected_skill)

        if kind == "authority-boundary":
            if not forbidden_actions:
                add_error(errors, f"{label} authority-boundary case must forbid an action")
        elif forbidden_actions:
            add_error(errors, f"{label} may use forbidden_actions only for authority-boundary cases")

        if isinstance(prompt, str) and kind == "direct" and isinstance(expected_skill, str):
            if f"${expected_skill}" not in prompt:
                add_error(errors, f"{label} direct prompt must invoke ${expected_skill}")
        elif isinstance(prompt, str) and kind in {"indirect", "negative"} and "$" in prompt:
            add_error(errors, f"{label} {kind} prompt must not invoke a skill by name")

        if (
            isinstance(prompt, str)
            and isinstance(expected_skill, str)
            and expected_skill in EXPLICIT_ONLY_SKILLS
            and f"${expected_skill}" not in prompt
        ):
            add_error(errors, f"{label} must explicitly invoke ${expected_skill}")

        if kind in coverage and isinstance(expected_skill, str) and expected_skill in valid_skills:
            coverage[kind].add(expected_skill)

    if seen_kinds != CASE_KINDS:
        missing = ", ".join(sorted(CASE_KINDS - seen_kinds))
        extra = ", ".join(sorted(seen_kinds - CASE_KINDS))
        add_error(
            errors,
            f"routing corpus kind coverage mismatch; missing={missing!r}, extra={extra!r}",
        )

    expected_coverage = {
        "direct": valid_skills,
        "indirect": valid_skills - EXPLICIT_ONLY_SKILLS,
        "authority-boundary": valid_skills,
    }
    for kind, covered_skills in coverage.items():
        if covered_skills != expected_coverage[kind]:
            missing = ", ".join(sorted(expected_coverage[kind] - covered_skills))
            add_error(errors, f"routing corpus {kind} coverage is missing: {missing}")

    if assembly_collision_coverage != ASSEMBLY_LINE_SPECIALISTS:
        missing = ", ".join(
            sorted(ASSEMBLY_LINE_SPECIALISTS - assembly_collision_coverage)
        )
        add_error(
            errors,
            "routing corpus Assembly Line collision coverage is missing: " + missing,
        )


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_skill_frontmatter(
    path: Path,
    text: str,
    errors: list[str],
) -> tuple[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        add_error(errors, f"{relative(path)} must begin with YAML frontmatter")
        return None

    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        add_error(errors, f"{relative(path)} has no closing frontmatter delimiter")
        return None

    frontmatter = lines[1:end]
    keys = [
        match.group(1)
        for line in frontmatter
        if (match := re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):(?:\s.*)?", line))
    ]
    if set(keys) != {"name", "description"} or len(keys) != 2:
        add_error(errors, f"{relative(path)} frontmatter must contain only name and description")

    name = ""
    description = ""
    index = 0
    while index < len(frontmatter):
        line = frontmatter[index]
        match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)", line)
        if match is None:
            index += 1
            continue
        key, raw_value = match.groups()
        if key == "name":
            name = unquote(raw_value)
        elif key == "description":
            if raw_value in {"|", ">", "|-", ">-"}:
                block: list[str] = []
                index += 1
                while index < len(frontmatter) and (
                    not frontmatter[index]
                    or frontmatter[index][0].isspace()
                ):
                    block.append(frontmatter[index].strip())
                    index += 1
                description = " ".join(part for part in block if part)
                continue
            description = unquote(raw_value)
        index += 1

    if not name:
        add_error(errors, f"{relative(path)} has an empty skill name")
    if not description:
        add_error(errors, f"{relative(path)} has an empty skill description")
    return name, description


def parse_simple_openai_yaml(
    path: Path,
    text: str,
    errors: list[str],
) -> tuple[dict[str, str], dict[str, str]]:
    if "\t" in text:
        add_error(errors, f"{relative(path)} must use spaces, not tabs")

    top_level = [
        match.group(1)
        for line in text.splitlines()
        if (match := re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):\s*", line))
    ]
    if not top_level or top_level[0] != "interface":
        add_error(errors, f"{relative(path)} must begin with an interface mapping")
    if not set(top_level).issubset({"interface", "policy"}):
        add_error(errors, f"{relative(path)} has an unsupported top-level key")

    sections: dict[str, dict[str, str]] = {"interface": {}, "policy": {}}
    current: str | None = None
    for line in text.splitlines():
        top_match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):\s*", line)
        if top_match:
            current = top_match.group(1)
            continue
        item_match = re.fullmatch(r"  ([A-Za-z_][A-Za-z0-9_-]*):\s*(.+)", line)
        if item_match and current in sections:
            key, raw_value = item_match.groups()
            sections[current][key] = unquote(raw_value)
        elif line.strip() and not line.lstrip().startswith("#"):
            add_error(errors, f"{relative(path)} contains unsupported YAML structure: {line!r}")

    return sections["interface"], sections["policy"]


def check_skills(errors: list[str]) -> None:
    skills_root = PLUGIN_DIR / "skills"
    if not skills_root.is_dir():
        add_error(errors, "plugin skills directory is missing")
        return

    actual = {
        path.name
        for path in skills_root.iterdir()
        if path.is_dir() and not path.is_symlink()
    }
    expected = set(EXPECTED_SKILLS)
    for missing in sorted(expected - actual):
        add_error(errors, f"required skill directory is missing: {missing}")
    for unexpected in sorted(actual - expected):
        add_error(errors, f"unexpected skill directory: {unexpected}")

    descriptions: dict[str, str] = {}
    display_names: dict[str, str] = {}

    for skill_name in EXPECTED_SKILLS:
        if SKILL_NAME_PATTERN.fullmatch(skill_name) is None or len(skill_name) > 64:
            add_error(errors, f"invalid expected skill name: {skill_name}")

        skill_path = skills_root / skill_name / "SKILL.md"
        if skill_path.is_file():
            text = read_text(skill_path, errors)
            if text is not None:
                parsed = parse_skill_frontmatter(skill_path, text, errors)
                if parsed is not None:
                    name, description = parsed
                    require_equal(name, skill_name, f"skill name for {skill_name}", errors)
                    if not 40 <= len(description) <= 800:
                        add_error(errors, f"{skill_name} description must contain 40 to 800 characters")
                    if description in descriptions:
                        add_error(
                            errors,
                            f"{skill_name} duplicates the description from {descriptions[description]}",
                        )
                    descriptions[description] = skill_name

                body = text.split("---", 2)[-1].strip()
                if len(body) < 200:
                    add_error(errors, f"{skill_name} instructions are too short to define a useful contract")
                if len(text.splitlines()) > 500:
                    add_error(errors, f"{skill_name} exceeds the 500-line instruction limit")

        yaml_path = skills_root / skill_name / "agents" / "openai.yaml"
        if yaml_path.is_file():
            text = read_text(yaml_path, errors)
            if text is not None:
                interface, policy = parse_simple_openai_yaml(yaml_path, text, errors)
                required_interface = {"display_name", "short_description", "default_prompt"}
                if set(interface) != required_interface:
                    add_error(
                        errors,
                        f"{relative(yaml_path)} interface keys must be exactly: "
                        + ", ".join(sorted(required_interface)),
                    )

                display_name = interface.get("display_name", "")
                short_description = interface.get("short_description", "")
                default_prompt = interface.get("default_prompt", "")

                if not 3 <= len(display_name) <= 64:
                    add_error(errors, f"{skill_name} display_name must contain 3 to 64 characters")
                if display_name in display_names:
                    add_error(
                        errors,
                        f"{skill_name} duplicates the display_name from {display_names[display_name]}",
                    )
                display_names[display_name] = skill_name

                if not 25 <= len(short_description) <= 64:
                    add_error(errors, f"{skill_name} short_description must contain 25 to 64 characters")
                if not 20 <= len(default_prompt) <= 240:
                    add_error(errors, f"{skill_name} default_prompt must contain 20 to 240 characters")
                if f"${skill_name}" not in default_prompt:
                    add_error(errors, f"{skill_name} default_prompt must mention ${skill_name}")

                if set(policy) != {"allow_implicit_invocation"}:
                    add_error(
                        errors,
                        f"{skill_name} policy must contain only allow_implicit_invocation",
                    )
                if policy.get("allow_implicit_invocation") not in {"true", "false"}:
                    add_error(errors, f"{skill_name} allow_implicit_invocation must be true or false")
                expected_policy = str(EXPECTED_IMPLICIT_POLICY[skill_name]).lower()
                if policy.get("allow_implicit_invocation") != expected_policy:
                    add_error(
                        errors,
                        f"{skill_name} allow_implicit_invocation must be {expected_policy}",
                    )


def check_python_policy(errors: list[str]) -> None:
    path = ROOT / "scripts" / "validate.py"
    text = read_text(path, errors)
    if text is None:
        return
    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        add_error(errors, f"validator has invalid Python syntax: {exc}")
        return

    for node in ast.walk(tree):
        modules: list[str] = []
        if isinstance(node, ast.Import):
            modules = [alias.name.split(".", 1)[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules = [node.module.split(".", 1)[0]]

        for module in modules:
            if module not in ALLOWED_PYTHON_MODULES:
                add_error(errors, f"validator imports a module outside its allowlist: {module}")
            if module in NETWORK_MODULES:
                add_error(errors, f"validator imports a blocked runtime module: {module}")


def main() -> int:
    errors: list[str] = []
    paths = repository_paths(errors)
    check_file_allowlist(paths, errors)

    for path in paths:
        text = read_text(path, errors)
        if text is not None:
            check_public_text(path, text, errors)

    check_plugin_manifest(errors)
    check_marketplace(errors)
    check_routing_cases(errors)
    check_skills(errors)
    check_python_policy(errors)

    unique_errors = sorted(set(errors))
    if unique_errors:
        print(f"Validation failed with {len(unique_errors)} error(s):")
        for error in unique_errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed for {PLUGIN_NAME}: {len(EXPECTED_SKILLS)} skills checked.")
    print(
        "Declarative routing expectations passed schema, consistency, and coverage "
        "checks; no agent or model behavior was executed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
