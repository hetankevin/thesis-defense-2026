# Thesis defense handoff

Updated November 18, 2026.

## Canonical project

Overleaf: https://www.overleaf.com/project/6afb7b39d9eebab656f22483
Private GitHub: https://github.com/hetankevin/thesis-defense-2026
Working copy: this directory. Publication clone: `/tmp/thesis-defense-linked-20261116`.
The surrounding proposal repository is archival and divergent. Commit locally there, but publish through the linked clone; do not blindly push the parent.

## Scope and standing corrections

49 main frames, 115 overlay pages, no backup. Kevin reached slide 31 at 45 minutes in rehearsal. We budget 20 more minutes for a 65-minute talk, leaving 25 minutes for questions. See timing.csv. The two themes are actor–critic learning and differentiable filtering, with a short connection to control.

November 18. Slide 21 presents the published rate with its attribution, assumptions and per-episode interpretation. Keep internal review comments out of the presentation. Shortened both technical sections and the control recap.

The current source supersedes the historical change logs below. The first three slides introduce the motivating questions. Slides 15–18 use the actor catching up to a fixed critic. Slides 27–44 move from the raw Dhaka series to the Bayes filter, particle approximation, off-parameter reweighting, score and fitting. Slide 44 reports a separate PyPOMP benchmark. The section ends with the original control diagram and a recap of the two themes. Both entry points compiled locally.

Keep the Dhaka cholera statistical inference application and its figures. Observations are monthly deaths. Never replace Wei Fan with Jianqing Fan. Preserve personal acknowledgments and author order. No notes carrying essential explanations, cute titles, invented results, or new experiments. Number RL algorithms. Use diagrams of actual operations, defined notation, stable reveals, and readable evidence.

## Concision pass, November 17

Revised prose across the opening, both technical sections and closing. Slide 13 puts the linear identity and hinge counterexample side by side; slide 15's diagram now carries the change from .2 to .8. Updated artifacts have 51 handout pages and 131 overlay pages. Rendered the whole handout and inspected staged reveals on slides 13, 15 and 43. Timing allocation is unchanged. Pre-edit Overleaf export matched d437646 across tracked files.

## November 17 afternoon revision

Title slide committee order: Yuting Wei (co-advisor), Giles Hooker (co-advisor), Enric Boix-Adserà. Slide 2 now introduces observed states and chosen actions in the robot example and monthly deaths and hidden populations in Dhaka.

- Slide 13 contrasts the sum of unclipped linear critics with a family of shifted hinges. The two bends illustrate failure of closure. The general product-cover upper bound is a separate argument, not a lower bound from the drawing. Slide 22 returns to the unclipped Tetris implementation.
- Slides 15–18 follow the same one-next-state example with zero reward, values 0 and 1, actor probabilities .2 and .8, and a fixed old critic of .4. Slide 23 gives the offline-data rate for the optimality-target variant.
- Slides 42–43 explain the before-resampling increment and label the empirical moments against zero. The Beamer overlay replaces only the inherited labels on Figure 1B. Plot data are unchanged.
- Rebuilt 51 handout frames and 133 overlay pages. Timing remains an allocation of 60 minutes. GitHub and local artifacts for this revision supersede the morning source. Safari was locked during the pre-sync check. Overleaf synchronization and server PDF verification are pending for this revision. The files named “overleaf” in output are the previous verified server build.

## Previous revision and review

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

Source revision `8a89fde` is pushed and merged in Overleaf. Both server builds succeeded: 134 overlays and 51 handout pages. Downloaded PDFs match local page text after whitespace normalization. Live slides 15 and 43 were rendered and inspected. Current `output/thesis-defense-overleaf-*` PDFs contain this reviewed revision. Preserve further live edits. The uncompiled old backup file is retained as historical source, not a delivery artifact.
