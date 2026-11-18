# Review against the presented deck

The supplied thesis-defense-overlays.pdf has 131 pages. A fresh build of df038f0 matches its extracted text on every page after whitespace normalization. The original file remains untouched.

Reviewed all changes in 8997b9a, 51a45f4 and 138fc40 against that baseline and Kevin's rehearsal feedback.

- Opening retained the simpler two-question roadmap, addressing the request to make slide 3 less technical.
- Actor–critic retained the corrected policy-update layout and moving-target/catch-up diagrams. Restored the max-cover inequality on 16, tracking error on 18, switch count before its cost bound on 20, and linear-critic interpretation on 22. These were lost during rewriting or excessive text cuts. Slide 21 presents the result with Kevin's common-class formulation. Removed the unsolicited proof-audit framing from the presentation.
- Filtering retained the Dhaka observations first, three-term Bayes formula, simulation/weighting/resampling diagrams and fixed-seed/fixed-parent explanation. Restored the integration-to-Monte-Carlo bridge, fitting objective, corrected log-likelihood definition and unit-weight derivative in main slide content. Replaced the undefined w3 reference with a sum over repeated copies.
- Evidence retained figure-specific labels and the verified GPU comparison, which Kevin requested. No new experiments were run.
- Closing retained the original PF-MCTQ diagram and broad recap. Restored the notation key alongside that diagram.
- Frame count stays 49, with 117 presentation pages. The 45-minute checkpoint at slide 31 is the user-reported observation. The later time allocation is an estimate.
- Theme, typography, source figures, title/committee and acknowledgments were not changed in these repairs.

Two independent reviewers compared the source changes with the presented deck. Both identified specific lost explanatory steps and recommended retaining the useful diagrams. Compiled both versions and inspected revised frames and representative reveals.
