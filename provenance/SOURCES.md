# Source and claim map

Current rehearsal revision: [source corrections and audience review](REHEARSAL_REVIEW.md), including the Tetris notebook, figure-specific qualifications and proof detail. It supersedes the historical notes below.

Original review 2026-11-16. No new experiments were run for this deck. Schematics illustrate operations and are not numerical results.

## Actor-critic

Kevin Tan, Wei Fan, Yuting Wei, *Actor-Critics Can Achieve Optimal Sample Efficiency*, ICML 2025, arXiv 2505.03710. Author source in the proposal provenance: `working/author_sources/2505.03710/`. Verified directly against the author manuscript `/Users/kevin/Downloads/Hybrid_RL_for_Linear_MDPs/actor_critic.tex`, including author block, Algorithm 2, Sections 3-4, hybrid extension, and experiment captions. The official ICML record is https://proceedings.mlr.press/v267/tan25c.html. The dissertation is not used as the authority for scientific claims.

Main slides 4-25: definitions, general-class obstruction, rare-switching construction, theorem and hybrid extension. The growing covering-number bound becoming vacuous is not an impossibility result. Main result uses SEC <= O(d log T). The detailed theorem and auxiliary regression class are in backup. No computational efficiency claim is made for optimistic confidence-set optimization.

- `actor-tracking.png`: paper `imgs/ac/ac_illustration.png`, figure label `fig:ac-illustration`. Original conceptual geometry. Added external legend and interpretation. Not measured regret.
- `actor-regret.jpg`: paper `imgs/ac/regret.jpg`, cumulative-regret experiment, 30 trials. Source y-axis erroneously says Reward. The slide covers that text with Cumulative regret, following the source caption/title. All data and bands preserved.
- `actor-hybrid.jpg`: paper `imgs/ac/hybrid.jpg`, AntMaze medium-diverse-v2. Main slide clips to the evaluation axes and legend (610bp left, 15bp bottom, 25bp right, 85bp top), with a LaTeX y-axis label, backup retains both panels. Smoothed trajectories. Deep implementation uses approximate optimism by action sampling; it is not the theoretical confidence-set algorithm.

## DMOP

Current GitHub `pypomp/dmop` source fetched 2026-11-16:
- `ms.tex` blob `25fbafb7351c10f62118a17b8ddb72e4799fd855`.
- `macros.tex` blob `ff1c0033a1aa5ab7ebd6d8b2e95cfdc74ce28072` supplies current title: *Automatic Differentiation for Inference on Partially Observed Markov Process Models*.
- Author order follows manuscript: K. Tan, A. J. Abkemeier, K. He, G. Hooker, E. L. Ionides.
- JRSS-B revise-and-resubmit status follows Kevin's explicit report; no acceptance inferred.

Main slides 26-46 use the current after-resampling score construction and `thm:mop-biasvar`, including the N^2(1-alpha)^2 discount-bias term and A6/A6-J derivative-stability requirements. These replace older versions of the error bound. Mathematical notation is simplified locally: tilde means predicted particles/weights, no tilde means after resampling.

Figures checked against current repository blobs:
- `dmop-local.png`: `imgs/095/mop.png`, Figure 1A (`fig:biasvar` left), blob `b6ff1d09496238e0d92cee7d8842f3e9d7f4e473`. Downloaded current figure because it differs from proposal asset. The reference likelihood is smooth; raw discontinuous PF evaluations are not plotted.
- `dmop-biasvar.png`: `imgs/095/biasvar.png`, Figure 1B, blob `22eceed644c42ea351780eae2c7deb3a60d4d3a7`. Existing asset exactly matches current blob.
- `dmop-searches.pdf`: `imgs/precise_raincloud.pdf`, comparable-effort panel of `fig:boxplot`, blob `336d1ce3926bbca1117e136b39e1d951d962df7f`. Existing asset exactly matches current blob. Values below -3800 omitted in source. This panel uses 100 searches per method with similar wall-clock budgets; timing excludes per-iteration diagnostic likelihood calls.

## Return to control

Tan and Xu, *From POMDP Theory to Deep RL with Particle Filters*, NeurIPS 2026 (accepted status supplied by Kevin). `control-pipeline.pdf` is the original `NeurIPS/Figures/pomdp_pipeline.pdf` from the author project `Particle_Filtering_for_POMDP`. Author block checked in `neurips_2026.tex`. No control theorem or experimental performance claim is added. Slide 49 distinguishes belief-tree analysis from the state-rollout implementation, following `NeurIPS/Sections/Sec3_MCTQ.tex` and `Sec5_Experiments.tex`. QMDP's assumption and computational motivation are explained before the pipeline.

## Other illustrations

All remaining diagrams are original TikZ schematics: decision paths, actor/critic data flow, critic update timeline, latent-state chain, particle propagation/selection, correction history, and cart velocities. They do not represent new empirical evidence. Bundled Saarland theme and Lato fonts are carried over unchanged from the proposal. Unused proposal images are retained as available assets but not shown.

## Proposal comparison and corrections in the second revision

The fresh proposal export `/Users/kevin/Downloads/Kevin_Tan___Proposal_Defense_2026/` is the narrative/figure reference. Its opening, RL, filtering, and references match the local proposal. Its newer personal acknowledgments were restored verbatim on slide 51. No proposal source was edited.

The initial thesis deck wrongly expanded Fan to Jianqing Fan. The paper's author block says Wei Fan; corrected everywhere. Slide 10 now constructs a pointwise optimistic critic rather than describing a single function selected by starting value. Slides 12-19 recover the accumulated-critic, policy-cover, stale-optimism, optimality-target, and tracking arguments from the proposal and manuscript.

The Dhaka application is retained. Current DMOP Section 4 identifies observations as monthly cholera deaths, not reported case counts. Slides 2 and 27 now say this. Slide 27 defines S, I, recovered stages, P, M, and diagram rates. No new disease-model claims or experiments were introduced.

Slide 37 distinguishes unit correction weights from observation weights. The error theorem remains the current after-resampling theorem, with model and derivative conditions attached. Empirical model performance is not presented as verification of the theorem's assumptions.

Additional restored figures: `franka-photo.jpg` (Ims, Wikimedia Commons, CC BY-SA 4.0) and `cholera-culture.jpg` (CDC PHIL 3906, public domain), both copied from the proposal. The original compartment diagram is `cholera.png`, DMOP figure label `fig:tikz-cholera`.

## Explanatory diagrams, November 16 evening

New TikZ diagrams are schematic explanations of the operations in the same verified actor-critic, DMOP, and control manuscripts above. They are not new experimental results. Original plotted evidence remains unchanged. In particular, categorical boundaries illustrate ancestor selection, the correction graph holds the baseline denominator fixed during differentiation, and the discount timeline weights log correction ratios along a lineage. It does not truncate simulated-state derivatives. The actor graph describes relative odds, not an absolute action-probability ordering. The control closing labels a next problem rather than claiming a composed guarantee.

## November 17: cold-review repairs (supersedes conflicting descriptions above)

The talk now has 51 frames, no compiled backups. References to absent backups were removed. The source for Algorithm 2 compares its current regression loss with a refit in F_h, as shown in the actual algorithm. G is separately identified as the auxiliary class containing expected backup targets. The general policy-cover bound becoming vacuous is explicitly distinguished from algorithmic failure. The trigger now precedes the reset-cost bound.

Slide 15 now uses a single-interval TikZ schematic of <f,pi_t> versus <f,pi_tau>, with one shaded missing term. This is explanatory geometry from the paper's old-policy tracking argument, not simulated or experimental data. The original actor-tracking image remains available but is not displayed.

The AntMaze explanation was corrected against the manuscript's Numerical experiments section: Alg. 2H takes a maximum over 10 sampled actions and omits policy resets; Alg. 1H uses a policy-evaluation target. The previous claim that both variants approximate optimism by action sampling was wrong. Neural soft actor-critic updates are not presented as an exact implementation of the theoretical algorithms. The Tetris source does not define its shaded-band statistic; the slide says so rather than guessing a confidence interval.

### Fig. 1A: actual reference and implementation

Current pypomp/dmop `code/fig1a/README.md`, `plot.py`, `curves.csv`, and `figure.mplstyle` retrieved via GitHub on November 17. README blob 3a15792a84584d496b06e78ca7f9e3957d3a099e. It identifies the reference curve as a particle-filter estimate, not true likelihood, and the illustration as 10,000-particle, before-resampling MOP with systematic resampling. Original model/filter notebook: hetankevin/diffPomp `cholera_mop.ipynb`, commit ab31c911ae223aa91eb4e216d7d33710103050c3.

`provenance/fig1a/` preserves the saved CSV and source plotting style. `plot.py` changes only labels, removes the large panel identifier, and uses five x ticks. It generates `figures/dmop-local-labeled.pdf`. No filtering experiment was rerun and no curve values were changed. Slide 42 names the estimator and resampling scheme prominently; it is not empirical verification of the after-resampling/multinomial theorem.

### Fig. 1B: score vector, normalization, and zero reference

Checked hetankevin/diffPomp `cholera_biasvar.ipynb` at both default commit 9e5aaa2b4dcdc453a94806967b5c9989c788b4bc and ab31c911ae223aa91eb4e216d7d33710103050c3. Cell 5 sets J=10000; cell 7 evaluates 1000 draws per alpha; cell 11 sums variance and squared means across score coordinates, and evaluates mean squared norm against ZERO. `optim.py` jgrad_mop differentiates mop_mean, which divides negative log likelihood by the number of observations. `filtering.py` mop_helper uses before-resampling increments and systematic resampling.

The existing PNG has the same curve geometry as cell 11's embedded output (different pixel resolution); it was not redrawn. The manuscript caption's description as a recovery-rate score is inconsistent with the plotting code's sum across coordinates. Slide 43 therefore identifies the mean-log-likelihood gradient vector in transformed coordinates and the zero reference. Interpreting squared deviation as bias requires a stationary fit. This is not an independently estimated reference score, and the slide does not claim stationarity was numerically certified.

### Comparable-time searches: correct cutoff, counts, and timing unit

Checked `Downloads/dmop-main/code/global_search/precise_report.qmd`, `dmop_search.py`, `prep.py`, and `exports/final_estimates.csv`, `exports/timings.csv` against the existing panel and manuscript median values. Cohort: comparable effort, n_monitors=1 for final estimates; n_monitors=0 for timing. The plotting code filters below -3780 (not -3800 as in the manuscript caption). Omitted counts: IF2 2/100, IFAD-1 4/100, IFAD-0 2/100, IFAD-.97 0/100. The red line is the maximum among the displayed comparison, not a separately supplied best-known likelihood.

The approximately 16-minute wall time is for the batch of 100 parallel searches per method, excluding diagnostic likelihood calls. It is not 16 minutes per individual search. Fit uses 5000 particles; retained run settings remain unchanged. The original panel is preserved, with the correct cutoff and omitted counts on the slide.

### November 17 follow-up

The Tetris implementation uses unclipped value estimates, as stated in the ICML paper, Numerical experiments. Slide 13's two-hinge example is an analytic illustration of lack of closure. It does not establish a regret or covering-number lower bound. The two-action numerical example on slides 15–18 illustrates the paper's old-policy optimism argument. Slide 23 uses the optimality-target variant of the non-optimistic hybrid theorem, with its own confidence width.

Slide 42's before-resampling increment is the normalized weighted sum of predicted-particle measurement densities (DMOP, Algorithm 1). On slide 43, the original plotted pixels for all three curves are preserved. The legend uses mean squared norm, squared norm of mean, and variance for the empirical zero-reference decomposition; at a stationary parameter the first two have the MSE and squared-bias interpretations.
