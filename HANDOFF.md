# Thesis defense handoff

Updated November 16, 2026.

## Canonical project

Overleaf: https://www.overleaf.com/project/6afb7b39d9eebab656f22483
Private GitHub: https://github.com/hetankevin/thesis-defense-2026
Local working copy: this directory. Linked publication clone: `/tmp/thesis-defense-linked-20261116`. The surrounding proposal repo is archival and has divergent history; do not blindly push it.

## Current scope

51 main frames plus 10 backups. 60-minute prepared talk in a 90-minute slot: opening 5, actor-critic 25, DMOP 25, control/closing 5. `timing.csv` totals 3600 seconds; this is an allocation, not a rehearsal. Actor-critic uses the single ICML paper and its hybrid extension. DMOP is the second topic. Control is a brief return to decision making, not a third full topic.

## User corrections that must persist

The first thesis delivery was rejected for invented attribution and generic prose/layout. Kevin's coauthor is Wei Fan, not Jianqing Fan. Use original author order and joint-work attribution. Restore personal acknowledgments from the live proposal. Do not infer contributors from writing samples.

Keep the Dhaka cholera application and its figures. Kevin explicitly objected when the agent misread his frustration as a request to remove it. The observation model is monthly cholera deaths, not case counts. Explain the statistical inference problem without an unrelated application detour.

Use direct titles, necessary definitions, actual method operations, equations and manuscript figures. No cute summaries, mandatory three-box chains, generic research slogans, or notes carrying essential explanations. Proposed RL algorithms are numbered.

## Changes in this revision

Replaced paragraph explanations across the deck with diagrams of actual operations: reward trajectories, critic regression and actor probabilities, accumulated critics and covering combinations, policy-evaluation versus optimality targets, resets and rejection tests, particle propagation/weighting/ancestry, moving categorical boundaries, fixed-ancestor differentiation, weight correction, discounting, and belief versus QMDP planning. Equations, assumptions, original experimental figures, Dhaka application, and personal acknowledgments remain.

The independent reviewer identified notation corruption on slide 17, label collisions, missing confidence/regret labels, overstatement of discounting and bound monotonicity, an implied composed control guarantee, and the immediate-reward wording of the actor update. All were corrected. Slide 7 now describes relative odds. Slides 16, 20, 23, 33, 36, and 37 were specifically reviewed for whether diagrams explain operations rather than merely arrange prose.

## Verification

Source checks remain recorded in `provenance/SOURCES.md`. All 61 handout pages were inspected in the diagram pass, then corrected pages were re-rendered. Representative intermediate reveals were inspected for slides 7, 16, 17, 32, 33, and 37. Independent findings and resolution are in `provenance/REVIEW.md`.

The latest Overleaf source was exported before editing at 18:01 Eastern and again at approximately 20:26 Eastern on November 16. All 39 tracked files matched linked commit e24c825 on both checks. No intervening live edits were found. The original proposal remains unchanged.

Final local builds: 144 overlay pages and 61 handout pages. No overfull, underfull, undefined-reference, or TeX errors. Existing imported-image DPI and PDF-version warnings remain. Timing still totals 3600 seconds (60 minutes), without a rehearsal. No new experiments or result plots were introduced.

Live synchronization and server PDF verification are pending for this diagram revision. Do not confuse the previous live exports with the current local PDFs until this line is updated.

## Build

Run `bash build.sh` with Tectonic. On Overleaf use XeLaTeX / TeX Live 2026. Open `main.tex` for overlays and `handout.tex` for one page per frame before compiling; the open standalone file can override the configured main-document choice. Restore main.tex after exporting.

## Delivery

Local PDFs are under `output/`. Final live PDF exports and previews will replace the previous versions after synchronization. A rehearsal is still needed to validate pacing. Do not treat compilation or independent review as Kevin's approval of presentation quality.
