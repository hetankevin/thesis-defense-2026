#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p build output
tectonic --keep-logs --keep-intermediates --outdir build main.tex
tectonic --keep-logs --keep-intermediates --outdir build handout.tex
cp build/main.pdf output/thesis-defense-overlays.pdf
cp build/handout.pdf output/thesis-defense-handout.pdf
