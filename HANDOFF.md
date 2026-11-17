# Thesis defense handoff

Updated November 17, 2026.

## Canonical project

Overleaf: https://www.overleaf.com/project/6afb7b39d9eebab656f22483
Private GitHub: https://github.com/hetankevin/thesis-defense-2026
Working copy: this directory. Publication clone: `/tmp/thesis-defense-linked-20261116`.
The surrounding proposal repository is archival and divergent. Commit locally there, but publish through the linked clone; do not blindly push the parent.

## Scope and standing corrections

51 main frames, no backup slides in either entry point. Title lines: Kevin Tan / Dissertation defense. Main research title unchanged. 60-minute prepared talk in the 90-minute slot: opening 5, actor–critic 25, DMOP 25, control/closing 5. This allocation is not a rehearsal. Actor–critic uses the ICML 2025 paper with Wei Fan and Yuting Wei, including its hybrid extension. DMOP is the other main topic; control is a short connection overview. Keep the original PF-MCTQ illustration.

Keep the Dhaka cholera statistical inference application and its figures. Observations are monthly deaths. Never replace Wei Fan with Jianqing Fan. Preserve personal acknowledgments and author order. No notes carrying essential explanations, cute titles, invented results, or new experiments. Number RL algorithms. Use diagrams of actual operations, defined notation, stable reveals, and readable evidence.

## Current revision

Implemented the cold review rather than leaving flags unresolved:

- Slides 12–13 connect reuse of data and adaptive regression targets to the growing policy cover. The vacuous bound is not called an impossibility result.
- Slide 15 uses a single fixed-critic interval and one missing tracking-error term, replacing the overloaded multi-curve illustration.
- Defined expected Bellman response before using its operator, promoted the confidence event, and connected the reset diagram to its initial KL cost.
- Regression test now comes before the rare-update/reset-cost bound. Comparator class is F_h as in the source algorithm. Target representability and computational scope are explicit on the guarantee slide.
- Hybrid coverage and the additional regret term are defined. AntMaze is explicitly a neural implementation comparison; only Alg. 2H takes the maximum over 10 sampled actions, and it omits resets.
- Differentiability and discounting motivations appear when used. Score-error randomness and normalization are explained.
- Recovered plotting sources for DMOP figures. Corrected the particle-filter likelihood reference, vector rather than recovery-only score diagnostic, mean-log-likelihood normalization, zero reference, resampling/increment differences, search cutoff (-3780), omitted counts, and batched timing unit. Details in `provenance/SOURCES.md`.
- Control closing identifies a connection overview; d=0 means no belief-tree lookahead. The original illustration remains.

No additional results were generated. Fig. 1A was redrawn from saved curve values with corrected labels and fewer ticks; code, data, and style are under `provenance/fig1a/`.

## Verification and review

Fresh Overleaf exports before editing and before synchronization both matched publication commit f4b7d6e across all tracked files. Safari reused extraction folder `Downloads/Thesis_Defense_2026-6`; the final export main.tex timestamp is November 17 09:35 UTC. No intervening edits were found.

Local builds: 134 overlay pages, 51 handout pages. Revised main slides and intermediate reveals for 12, 15, 19, and 43 were rendered and inspected. The latest build has no overfull/underfull, undefined-reference, or TeX errors. Existing image-resolution/PDF-version warnings persist. Timing remains 3600 seconds.

Independent reviewer used rendered slides alone. Original findings: `provenance/COLD_STAT_AUDIENCE_REVIEW_2026-11-17.md`. Re-review and final verification: `provenance/REASONING_REWRITE_REVIEW_2026-11-17.md`. Verdict: core argument followable with normal narration, previous actor–critic blockers resolved, final three presentation issues addressed, no new layout blockers. This is an audience review, not a replacement for source verification or Kevin's judgment.

## Build and delivery

Run `bash build.sh` (Tectonic). Overleaf uses XeLaTeX/TeX Live 2026. Open main.tex for overlays or handout.tex for one page per frame; restore main.tex after exports. Build artifacts and previews are under `output/` (ignored by Git).

Current source is ready for synchronization; server PDFs must be downloaded and compared with local builds before marking delivery complete. Preserve further live edits. The uncompiled old backup file is retained as historical source, not a delivery artifact.
