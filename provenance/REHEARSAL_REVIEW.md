# Rehearsal revision and independent review

Historical review of the November 17 version. Kevin subsequently requested a shorter theorem slide. The November 18 deck presents the published result.

## Source corrections

**Actor–critic proof.** Algorithm 2 fits in the critic class F. Assumption 2 places expected optimality backups in an auxiliary class G. Lemma 14(i), Equation (66), uses a backup as an admissible member of a critic confidence set. Membership in G alone does not justify this step. Take two stages, one state, one action, zero rewards and no retained data. Set F₁={0}, F₂={0,1}, G₁={0,1} and include the zero terminal target in G₂. The optimal value zero is realizable and every required backup lies in G. The upper critic has f₁=0 and f₂=1, so its first-stage expected backup is 1. This refutes the pointwise step under the stated assumptions. Regret in this example is zero. Whether the regret theorem admits a different proof remains open in this audit. Slide 21 states the limitation on the same reveal as the rate. [Published paper, Lemma 14](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25c/tan25c.pdf#page=30)

**Tetris.** The plotting notebook computes cumulative reward shortfall relative to −0.25 per move, with mean and one standard deviation across 30 trials. This differs from regret relative to an optimal policy. Slide 22 replaces the source title and axis label accordingly. The unclipped linear critics add to one coefficient vector. The hinge example on slide 13 illustrates how that property can fail. [Author repository, actor_critic.ipynb](https://github.com/hetankevin/hybridcov)

**Dhaka.** Slide 27 plots the 600 original monthly observations. Its two columns are the decimal-year observation times and death counts. The process diagram on slide 28 is the paper’s compartment illustration. [Original data](https://github.com/pypomp/pypomp/blob/main/pypomp/data/dacca/dacca.csv)

**Filter.** Months are indexed by n, particles by j and the two parameters by θ and φ. The baseline randomness is shared and the parent indices replayed. Slide 35 takes an expectation conditional on the predicted particles. Slide 36 shows the sampled counterpart. The secant and tangent illustrate the after-resampling construction. The score estimator is mean-square consistent with full corrections as the number of particles grows, for fixed data under the assumptions on slide 41. At a fixed discount below one, the bias bound can persist. [Updated manuscript, Sections 3–5 and Theorem 5](https://arxiv.org/html/2407.03085v2)

**Filter figures.** The identity at the baseline refers to matched randomness within one construction. Saved curves in Fig. 1A have slightly different numerical estimates at 18. Fig. 1B measures the empirical second moment of the mean-log-likelihood gradient across all transformed coordinates, relative to zero. Both use before-resampling increments and systematic resampling. Theorem 5 treats after-resampling increments with multinomial resampling. Fig. 3 and Table 1 report the comparable-time search experiment. The timing bars on slide 44 measure a separate filter batch. See [GPU_BENCHMARK.md](GPU_BENCHMARK.md).

**Control.** The PF-MCTQ diagram is the authors’ original illustration. The bound on structural error decreases geometrically with belief-tree depth. The implementation uses zero belief-tree lookahead and state rollouts. Sec4 in the author’s Particle_Filtering_for_POMDP source gives the depth dependence.

## Independent audience checks

A statistics reader unfamiliar with RL and particle filtering and an ML reader unfamiliar with statistical filtering independently read the compiled slides without notes, manuscripts or source. Both could reconstruct the moving-target argument, conditional maximum inequality, uniform restart, monthly bootstrap filter and distinction between holding random numbers fixed and replaying ancestors.

The first pass found a missing link between expectation and realized resampling, identical particle positions for the perturbed run, an ambiguous secant/tangent, and a rate presented before its missing proof premise. A cropped Tetris title and overlapping timing-chart labels were visible in the rendered slides. The next pass checked the rebuilt diagrams and staged reveals. Its final requests were to put the qualification on the first reveal of slide 21, name the newly filtered state on slide 29, and distinguish a bound from measured planning error on slide 47. All three edits were applied. A separate manuscript and data check caught the small discrepancies between empirical estimates at the baseline in Fig. 1A.

## Pacing

Kevin reported reaching slide 31 at 45 minutes. The timing sheet treats this as the end of that slide, distributes 45 minutes across slides 1–31, and allocates 20 minutes to finish. Individual times and the 65-minute total are estimates pending a full rehearsal of the new deck.

Final check: both readers approved the frozen handout and presentation after visually rechecking the affected reveals.
