# Thesis defense handoff

Updated November 20, 2026.

## November 20 additions

Downloaded the current Overleaf source (`/Users/kevin/Downloads/Thesis_Defense_2026-14`) and preserved Kevin's edits by pushing from Overleaf to GitHub, then fast-forwarding this checkout to `a7c48bd` (`save live slide edits`). These edits rename and revise the opening, actor-critic and filtering slides and remove the old optimism frame. Preserve Kevin's wording, including informal titles and deliberate capitalization.

Added exactly the requested material using pre-insertion slide numbers:
- After slide 14: attached screenshot, unchanged, titled “Doesn't work” (new 15).
- After slide 40, “Fitting the model”: current DMOP Figure 5 optimization curves (new 42).
- After slide 41, “Likelihood searches for the Dhaka cholera model”: all five panels of current Figure S.14, split into A–C and D–E for readability (new 44–45).

Both local variants compile without overfull/underfull boxes or TeX errors. Rendered and inspected all four additions. There are 52 main slides and 123 overlay pages, no backup. Timing rows follow Kevin's new frame order and titles; retained allocations unchanged, with 20+50+45+45 seconds for the additions, totaling 3985 seconds (66m25s). This is an allocation, not a rehearsal. Independent review confirmed complete figures and caption fidelity; identified and fixed the need to label Figure 5 as the extended fitting-budget experiment. Fresh pre-sync source export still matches `a7c48bd`. Source through `e93663a` merged into Overleaf; the dialog reported no new GitHub commits. Server downloads `Thesis_Defense_2026-28.pdf` (123 overlays) and `-29.pdf` (52 handout pages) match local builds on every page after whitespace normalization. Rendered and inspected all four additions from the server handout. Verified PDFs are in `output/thesis-defense-overleaf-{overlays,handout}.pdf`, preview `output/nov20-additions.png`. Overlay entry point restored.

## Current revision, November 19

Kevin released the Overleaf hold with “ok update overleaf.” A fresh live source export at `/Users/kevin/Downloads/Thesis_Defense_2026-13` matches publication commit `691f874` across existing tracked files. Preserve any subsequent live changes through GitHub Sync.

Rebuilt the fixed-seed explanation: likelihood jumps when parent selection changes away from the baseline; fixed-parent reweighting gives a smooth local approximation and its derivative. Moved the two likelihood-correction equations onto that slide and removed their redundant standalone frame. The next slides distinguish the unchanged forward pass from the approximate score and explain why undiscounted off-parameter weight products motivate discounting. Added the London runtime comparison with sampler qualifications. Control now starts with “Let's deal with control now”; QMDP's future-state observability assumption precedes its formula. The control pipeline explicitly connects earlier model fitting, standard PF inference, and planning. The following slide shows published MuJoCo Ant/HalfCheetah results under both masks, including original Ant instability and the unfavorable HalfCheetah position-masked result.

Historical hold statements below describe earlier revisions and are superseded by this release. Local build: 49 handout slides, 120 overlay pages; 3900 seconds (65 minutes), including 60 seconds for MuJoCo. Inspected revised slides and intermediate reveals, resolved layout warnings, and obtained independent source/clarity reviews. Source through `e77a7d6` merged into Overleaf, which reported no new GitHub commits. Recompiled both entry points on the server and downloaded `Thesis_Defense_2026-26.pdf` (120 overlay pages) and `-27.pdf` (49 handout pages). Page counts and whitespace-normalized extracted text match local builds on every page. Rendered and inspected revised server handout pages. Verified server PDFs are in `output/thesis-defense-overleaf-{overlays,handout}.pdf`; previews are `output/{filtering,control}-revision.png`. Overlay entry point restored.

## Canonical project

Overleaf: https://www.overleaf.com/project/6afb7b39d9eebab656f22483
Private GitHub: https://github.com/hetankevin/thesis-defense-2026
Working copy: this directory. Publication clone: `/tmp/thesis-defense-linked-20261116`.
The surrounding proposal repository is archival and divergent. Commit locally there, but publish through the linked clone; do not blindly push the parent.

## Baseline and revision

The PDF Kevin presented is /Users/kevin/Downloads/thesis-defense-overlays.pdf. All 131 pages match the whitespace-normalized extracted text of a fresh build at df038f0. This is the baseline for reviewing later changes. The revision restores the max-cover inequality, actor tracking gap, switch-count placement, linear-critic interpretation, corrected log-likelihood definition, unit-weight derivative and control-figure notation. See provenance/BASELINE_REVIEW.md.

## Latest notation correction, November 19

Slide 13 uses Kevin’s requested $\mathcal{N}_{\mathcal{F}}(\epsilon)$ throughout in place of $M$, including the sequence count and bound. Both PDF variants rebuilt and the slide’s reveals visually checked. Overleaf hold remains in force.

## Latest visual review, November 19

Inspected all 49 frames and all 121 overlay pages. Fixed diagram-label spacing on 6, 9, 31, 35 and 46; made the original control figure’s planning label larger on 47; enlarged the likelihood legend on 39. Source/qualification notes are larger and darker. Independent re-review found no remaining blocking defects. Both versions rebuilt without overfull/underfull boxes or TeX errors. No papers, equations, results or timing allocations were changed. See `provenance/VISUAL_REVIEW_2026-11-19.md`. Overleaf was not accessed; the explicit hold above remains in force.

## Scope and standing corrections

Latest revision: whole-deck language pass following Kevin's “look at the whole presentation.” Read all 49 slides and revised phrasing across the opening, actor–critic section, filtering section and closing. Replaced clipped instructions with explanations of why the operations are needed; tied the Bayes update to observed deaths; shortened several PF titles and the final recap. Mathematical displays, assumptions, figures and reported findings are preserved. Slide 31 still uses unnumbered bars.

Both local versions compile: 49 handout pages and 121 overlay pages. Inspected the entire rendered handout and representative reveals. Timing stays at 3900 seconds (65 minutes). No overfull/underfull boxes or compile errors. An independent whole-deck language review identified repetitions on slides 25, 36 and 37; these were removed. It also suggested plainer wording for AntMaze and QMDP, which was adopted. Current PDFs are `output/thesis-defense-handout.pdf` and `output/thesis-defense-overlays.pdf`.

Overleaf is pending: Safari now opens, but the defense tab reports “You're offline” and says edits are saved in the browser. No reload, upload or pull was attempted, to preserve those edits. Before syncing, wait for reconnection, export source, compare it with publication history, and merge any live edits. The last verified live source is `691f874`; files named `overleaf` remain those older verified server builds. GitHub is updated through the local publication checkout. Historical delivery statements below apply only to their named revisions.

November 18, latest correction: Kevin rejected worked arithmetic as a teaching device. His example: keep slide 31's S/I/R counts and modeled deaths, then an arrow determined by measurement density leading to an unnumbered normalized-weight profile. Numbers may illustrate states, but the audience should not have to follow fabricated numerical calculations. This applies across the deck.

Replaced the density values, numerical correction ratios, calculated likelihood, toy affine density and numerical derivative on slides 31 and 33–38. The figures now explain measurement weighting, fixed-parent reweighting, accumulation across copies, unit values with nonzero derivatives, and discounting. Essential symbolic method equations remain. Slide 30's compartment counts and the state-copy diagrams remain as visual context. The RL section already uses conceptual moving-target and catch-up diagrams; its hinge sketch now labels thresholds u1/u2 instead of arbitrary decimal values. Experimental plots and reported numerical results are unchanged. Independent review confirmed that the operations can be explained by pointing at the figures without arithmetic. Removed the redundant derivative recurrence on slide 38, leaving the timeline and weight update.

The arithmetic-based correction example in earlier revisions is superseded. It must not be restored just because it passed a correctness check. Visual explanation and presenter effort are part of the review criterion.

49 main frames, 121 overlay pages, no backup. Kevin reached slide 31 at 45 minutes in rehearsal. We budget 20 more minutes for a 65-minute talk, leaving 25 minutes for questions. See timing.csv. The two themes are actor–critic learning and differentiable filtering, with a short connection to control.

November 18. Slide 21 presents the published rate with its attribution and per-episode interpretation, taking the same class for critics and their backups. Keep internal review comments out of the presentation. Shortened both technical sections and the control recap.

The current source supersedes the historical change logs below. The first three slides introduce the motivating questions. Slides 15–18 use the actor catching up to a fixed critic. Slides 27–44 move from the raw Dhaka series to the Bayes filter, particle approximation, off-parameter reweighting, score and fitting. Slide 44 reports a separate PyPOMP benchmark. The section ends with the original control diagram and a recap of the two themes. Both entry points compiled locally. The final language pass replaces staged questions and generic takeaway prose with direct descriptions of the operations, retaining the equations and diagrams. The 117-page Overleaf overlay PDF matches the local build page by page after whitespace normalization. Source through d141c39 was merged into Overleaf, which reported no new GitHub commits after the merge.

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
