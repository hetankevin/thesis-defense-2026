# Thesis defense handoff

Updated November 17, 2026.

## Canonical project

Overleaf: https://www.overleaf.com/project/6afb7b39d9eebab656f22483
Private GitHub: https://github.com/hetankevin/thesis-defense-2026
Local working copy: this directory. Linked publication clone: `/tmp/thesis-defense-linked-20261116`. The surrounding proposal repo is archival and has divergent history; do not blindly push it.

## Current scope

51 main frames, with no backup slides in either compiled version. 60-minute prepared talk in a 90-minute slot: opening 5, actor-critic 25, DMOP 25, control/closing 5. `timing.csv` totals 3600 seconds; this is an allocation, not a rehearsal. Actor-critic uses the single ICML paper and its hybrid extension. DMOP is the second topic. Control is a brief return to decision making, not a third full topic.

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

Reviewed source commit `33851e9` is pushed to GitHub and merged in Overleaf. Both live XeLaTeX builds succeeded: 144 overlay pages and 61 handout pages. Downloaded server PDFs match local page text after whitespace normalization. Live pages 16, 32, and 37 were rendered and visually checked. The current `thesis-defense-overleaf-*` files contain this diagram revision.

## Build

Run `bash build.sh` with Tectonic. On Overleaf use XeLaTeX / TeX Live 2026. Open `main.tex` for overlays and `handout.tex` for one page per frame before compiling; the open standalone file can override the configured main-document choice. Restore main.tex after exporting.

## Delivery

Local and verified live PDFs are under `output/`. `slide-07.png`, `slide-16.png`, `slide-17.png`, `slide-27.png`, `slide-32.png`, `slide-33.png`, `slide-37.png`, `slide-39.png`, and `slide-46.png` are rendered from the current live handout. Source ZIPs are refreshed from the linked repository. A rehearsal is still needed to validate pacing. Do not treat compilation or independent review as Kevin's approval of presentation quality.

## Follow-up inspection: language and layout

Inspected all 61 current server-rendered handout pages and read their slide text. Replaced vague or performative titles with the actual subject on 13, 17, 20, 25, 37, 46, and 47. Kept genuine explanatory questions such as the actor-critic introduction and the differentiation obstacle. Removed “hides,” “drops out,” “tiny,” and “critic prefers” phrasing. Clarified total reward and log likelihood on the roadmap, covering-number counts, and ancestor indices. Avoided using “score” for ordinary measurement-density evaluation because score later means a log-likelihood derivative.

Moved slide 8 labels above the computation so arrows do not cross them. Cleared dashed guides from the fixed-ancestry label on 34. Re-rendered every changed frame. Technical equations, source figures, paper selection, Dhaka application, and timing are retained. Local builds: 144 overlays, 61 handout pages, no layout or undefined-reference warnings. Current live source was exported and compared with 5291bb6 before editing; all 39 files matched. Revision `4b801d3` is pushed and merged in Overleaf. Both server builds succeeded (144 overlay pages, 61 handout pages) and match local page text. Downloaded live pages 8, 13, and 37 were inspected. Updated previews and source ZIP are in `output/`.

## November 17: title and no backups

Kevin requested the title lines “Kevin Tan” and “Dissertation defense.” Updated those lines and removed the appendix input from both entry points. The old backup source is retained uncompiled. A fresh Overleaf export (`Thesis_Defense_2026-5`) matched all 39 tracked publication files before editing. Local builds produce 51 handout pages and 132 overlay pages. The title was visually inspected; pages 2–51 have unchanged extracted text. The cold statistical-audience review is underway and will be recorded separately; its findings are not yet implemented.
