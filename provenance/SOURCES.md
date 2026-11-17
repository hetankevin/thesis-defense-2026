# Source and claim map

Reviewed 2026-11-16. No new experiments were run for this deck. Schematics illustrate operations and are not numerical results.

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
