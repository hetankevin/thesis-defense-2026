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

Rebuilt opening, restored proposal examples and acknowledgments, corrected authors, replaced the starting-value description with pointwise optimism, restored the accumulated-critic/policy-cover calculation and optimism reasoning, clarified stale-policy error and resets, defined Dhaka compartments and observations, distinguished correction weights from observation weights, enlarged the AntMaze panel, and distinguished control theory from experimental rollouts. Removed rounded filled diagram styling and several redundant text-box diagrams.

## Verification

Sources and scientific checks: `provenance/SOURCES.md`. Independent review: `provenance/REVIEW.md`. All handout pages inspected, then changed pages rechecked. Representative intermediate overlays inspected. No new experiments were run.

Latest live source was downloaded before editing and again at approximately 17:48 Eastern. All 37 tracked files matched linked GitHub commit 423cc73. No intervening Overleaf edits were found. The original proposal is untouched.

Final local builds succeed: 142 overlay pages and 61 handout pages, with no overfull, underfull, undefined-reference, or TeX errors. Source JPEG DPI and imported PDF-version warnings remain benign. Final targeted pages and representative reveals were rendered and inspected. Live synchronization is pending; older `thesis-defense-overleaf-*` files must not be treated as revised until replaced.

## Build

Run `bash build.sh` with Tectonic. On Overleaf use XeLaTeX / TeX Live 2026. Open `main.tex` for overlays and `handout.tex` for one page per frame before compiling; the open standalone file can override the configured main-document choice. Restore main.tex after exporting.

## Remaining delivery steps

Finish final render checks, commit/push canonical source, pull into Overleaf, compile both live versions, download and compare them with local builds, update this status, and deliver the revised handout plus examples.
