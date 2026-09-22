# Independent Evidence

Prefer evidence the vendor did not produce. For each source, record the date
checked, the exact configuration tested and whether the result is a single run.

## Where to look

Confirm each source is still maintained and that its method has not changed.
These names are pointers, not endorsements.

| Question | Kinds of source |
| --- | --- |
| Real software work | SWE-bench Verified and harder successors such as SWE-bench Pro, Terminal-Bench, Aider's polyglot benchmark |
| Fresh, low-contamination coding | Date-bounded sets such as LiveCodeBench |
| Long, multi-step autonomy | METR task time-horizon measurements |
| Tool use and agents | The tau-bench family, the Berkeley Function Calling Leaderboard, OSWorld for computer use |
| Hard reasoning and knowledge | GPQA Diamond, Humanity's Last Exam, ARC-AGI on held-out sets |
| Long context | Multi-round coreference and needle-style suites run near the claimed window |
| Factuality | SimpleQA-style sets and hallucination leaderboards |
| Price, speed and tokens used | Artificial Analysis, which also reports the tokens a model spends on its index |
| Human preference | LMArena with style control; preference is not correctness |
| Cross-benchmark trackers | Epoch AI, LiveBench |

## Reading it

- On day one many independent-looking numbers are vendor-supplied or single
  runs. Mark them provisional and set a recheck, usually one to two weeks out.
- Weight benchmarks that match the actual work. A reasoning gain says little
  about review recall on a particular codebase.
- Record the effort and scaffold behind each number. Two leaderboards can rank
  the same models differently because their settings differ; report both rather
  than choosing the flattering one.
- Community reports are leads. Keep the ones with reproducible prompts, versions
  and outputs, and test a claim before relying on it.
- The absence of an independent result is recorded as absence, never as
  confirmation.
