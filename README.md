# Thesis defense

Two topics: actor-critic learning (Tan, Fan, Wei, ICML 2025) and differentiable particle filtering (Tan, Abkemeier, He, Hooker, Ionides). Brief return to particle-based control at the end.

52 slides, 123 overlay pages. The pacing sheet allocates 66 minutes 25 seconds, leaving about 24 minutes for questions in the 90-minute slot. This includes the November 20 figure additions. Only Kevin's earlier 45-minute checkpoint at the particle-filter example was measured; the current full-deck allocation has not been rehearsed.

## Build

Use XeLaTeX on Overleaf, main document `main.tex` (overlays) or `handout.tex` (one page per frame). Fonts and theme are included.

Locally, run `bash build.sh` with Tectonic installed. PDFs are written to `output/`.

See `HANDOFF.md`, `timing.csv`, and `provenance/SOURCES.md`.

## Live project

[Overleaf](https://www.overleaf.com/project/6afb7b39d9eebab656f22483) is linked to the private [thesis-defense-2026 repository](https://github.com/hetankevin/thesis-defense-2026). This is the canonical location for future revisions. Open the desired standalone TeX file before compiling.
