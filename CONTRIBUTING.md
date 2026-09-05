# Contributing

Contributions should keep Ranger Foundry small, predictable, and safe to use in an unfamiliar repository.

## Before opening a change

1. Choose one clear capability and one clear trigger boundary.
2. Confirm that an existing skill cannot handle the request with a small improvement.
3. Keep organization-specific and environment-specific rules outside the public core.
4. Contribute only material you have the right to license under MIT.
5. Avoid credentials, private data, personal identifiers, internal paths, and environment identifiers.

## Skill contract

Every skill must:

- live in one of the approved directories under `plugins/ranger-foundry/skills/`;
- include a `SKILL.md` with only `name` and `description` in its frontmatter;
- include `agents/openai.yaml` with useful display text and a default prompt;
- use the directory name as its skill name;
- state what it produces and what it is not authorized to change;
- defer to repository-local instructions and more specific overlays;
- remain useful across languages, frameworks, and delivery platforms.

Keep detailed reference material out of the initial bundle. Add supporting files only after the repository policy and validator are deliberately expanded.

## Validation

Run:

```bash
   python3 -I scripts/validate.py
```

The same command runs in continuous integration. A change is not ready while validation reports an error.

## Review expectations

Reviewers evaluate trigger precision, authority boundaries, behavioral usefulness, public safety, interaction with neighboring skills, and test coverage. Follow [docs/skill-review.md](docs/skill-review.md).

Use focused commits and describe the user-visible behavior that changed. Do not combine unrelated skill changes in one pull request.
