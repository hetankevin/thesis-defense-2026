# Source and claim map

Reviewed 2026-11-16. No new experiments were run for this deck. Schematics illustrate operations and are not numerical results.

## Actor-critic

Tan, Fan, Wei, *Actor-Critics Can Achieve Optimal Sample Efficiency*, ICML 2025, arXiv 2505.03710. Author source in the proposal provenance: `working/author_sources/2505.03710/`. Cross-checked current dissertation `chapters/ch04-actor-critic.tex` under `UMich/Research/dissertation`.

Main slides 4-24: definitions, general-class obstruction, rare-switching construction, theorem and hybrid extension. The growing covering-number bound becoming vacuous is not an impossibility result. Main result uses SEC <= O(d log T). The detailed theorem and auxiliary regression class are in backup. No computational efficiency claim is made for optimistic confidence-set optimization.

- `actor-tracking.png`: paper `imgs/ac/ac_illustration.png`, figure label `fig:ac-illustration`. Original conceptual geometry. Added external legend and interpretation. Not measured regret.
- `actor-regret.jpg`: paper `imgs/ac/regret.jpg`, cumulative-regret experiment, 30 trials. Source y-axis erroneously says Reward. The slide covers that text with Cumulative regret, following the source caption/title. All data and bands preserved.
- `actor-hybrid.jpg`: paper `imgs/ac/hybrid.jpg`, AntMaze medium-diverse-v2. Main slide clips to evaluation panel, backup retains both panels. Smoothed trajectories. Deep implementation uses approximate optimism by action sampling; it is not the theoretical confidence-set algorithm.

## DMOP

Current GitHub `pypomp/dmop` source fetched 2026-11-16:
- `ms.tex` blob `25fbafb7351c10f62118a17b8ddb72e4799fd855`.
- `macros.tex` blob `ff1c0033a1aa5ab7ebd6d8b2e95cfdc74ce28072` supplies current title: *Automatic Differentiation for Inference on Partially Observed Markov Process Models*.
- Author order follows manuscript: K. Tan, A. J. Abkemeier, K. He, G. Hooker, E. L. Ionides.
- JRSS-B revise-and-resubmit status follows Kevin's explicit report; no acceptance inferred.

Main slides 25-45 use the current after-resampling score construction and `thm:mop-biasvar`, including the N^2(1-alpha)^2 discount-bias term and A6/A6-J derivative-stability requirements. These replace older versions of the error bound. Mathematical notation is simplified locally: tilde means predicted particles/weights, no tilde means after resampling.

Figures checked against current repository blobs:
- `dmop-local.png`: `imgs/095/mop.png`, Figure 1A (`fig:biasvar` left), blob `b6ff1d09496238e0d92cee7d8842f3e9d7f4e473`. Downloaded current figure because it differs from proposal asset. The reference likelihood is smooth; raw discontinuous PF evaluations are not plotted.
- `dmop-biasvar.png`: `imgs/095/biasvar.png`, Figure 1B, blob `22eceed644c42ea351780eae2c7deb3a60d4d3a7`. Existing asset exactly matches current blob.
- `dmop-searches.pdf`: `imgs/precise_raincloud.pdf`, comparable-effort panel of `fig:boxplot`, blob `336d1ce3926bbca1117e136b39e1d951d962df7f`. Existing asset exactly matches current blob. Values below -3800 omitted in source. This panel uses 100 searches per method with similar wall-clock budgets; timing excludes per-iteration diagnostic likelihood calls.

## Return to control

Tan and Xu, *From POMDP Theory to Deep RL with Particle Filters*, NeurIPS 2026 (accepted status supplied by Kevin). `control-pipeline.pdf` is the original `NeurIPS/Figures/pomdp_pipeline.pdf` from the author project `Particle_Filtering_for_POMDP`. Author block checked in `neurips_2026.tex`. No control theorem or experimental claim is added. QMDP's assumption and computational motivation are explained before the pipeline.

## Other illustrations

All remaining diagrams are original TikZ schematics: decision paths, actor/critic data flow, critic update timeline, latent-state chain, particle propagation/selection, correction history, and cart velocities. They do not represent new empirical evidence. Bundled Saarland theme and Lato fonts are carried over unchanged from the proposal. Unused proposal images are retained as available assets but not shown.
