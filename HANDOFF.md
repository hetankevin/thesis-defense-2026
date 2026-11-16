# Thesis defense handoff

Updated November 16, 2026.

## Canonical project

Overleaf: https://www.overleaf.com/project/6afb7b39d9eebab656f22483
Linked private GitHub repository: https://github.com/hetankevin/thesis-defense-2026
The proposal-defense repository copy is archival. Preserve live edits by exporting and comparing before future changes.

## Scope and pacing

49 main frames plus 10 backup frames. Target 60 minutes in a 90-minute slot: opening 5, actor-critic 25, filtering 25, control/closing 5. `timing.csv` totals 3600 seconds. This is an allocation, not a rehearsal.

RL uses only Tan, Fan, Wei's ICML 2025 actor-critic paper and its own hybrid extension. The second topic is DMOP. Four closing frames connect filtering to control and summarize the two contributions. The other proposal projects are not included. Audience: broad statistics, with definitions and essential explanations on slides and no required speaker notes.

## Sources and argument

See `provenance/SOURCES.md` for manuscript and figure provenance. RL develops values, regression, policy updates, growing critic history, stale optimism, optimality targets, rare updates/resets, tracking, and the guarantee. It distinguishes the optimism-free hybrid theorem from the approximate-optimism neural experiment.

Filtering develops hidden states, likelihood, prediction/weighting/resampling, fixed ancestors, correction weights, their first-step cancellation, informative derivatives, discounting, and optimization. The current manuscript's error theorem and derivative-stability assumptions replace older versions. Control preserves the original PF-MCTQ diagram and explains QMDP's computational motivation.

## Review and verification

Independent slides-alone review completed. See `provenance/REVIEW.md`. Findings addressed: observation feedback arrow, theorem/experiment distinction, missing correction cancellation, runtime matching description, and MCTS expansion. The follow-up found no material comprehension issue; its remaining underbrace-label spacing issue was fixed and visually checked.

Both final local versions compile: 134 overlay pages and 59 handout pages. No overfull, underfull, or undefined warnings. Benign source JPEG DPI and imported PDF version warnings remain. All initial pages were visually inspected, then every revised frame was re-rendered and checked. Representative intermediate reveals were checked for stable positioning.

The preceding live Overleaf exports had 131/58 pages and matched the preceding local handout text on every page. Before this review update, a new Overleaf source download was compared against all 36 tracked files in linked GitHub commit b01df96: no differences. The final review update is ready for live compilation and export.

## Build and delivery

Overleaf: XeLaTeX, TeX Live 2026. Open `handout.tex` explicitly before compiling handouts and `main.tex` before overlays: Overleaf may compile the open standalone file even when the main-document setting names another file. Restore main.tex when finished.

Local build: `bash build.sh` with Tectonic. PDFs and source ZIP are under `output/`. Files prefixed `thesis-defense-overleaf-` are downloaded live exports. Refresh those after syncing review fixes.

Next: synchronize the reviewed commit, verify both live builds and downloaded handout text, then record final delivery. A rehearsal remains necessary to validate delivery pace.
