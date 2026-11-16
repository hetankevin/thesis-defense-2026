# Thesis defense handoff

2026-11-16. Separate deck, leaving proposal source unchanged. 48 main frames + 10 backup. Target 60 minutes in 90-minute slot. Timing.csv totals 3600 seconds: 5/25/25/5 minutes. Not rehearsed.

Main selection: only ICML actor-critic paper and its own hybrid extension in RL; DMOP for second main topic; four-slide return to control/closing. Other dissertation projects are not silently added. Audience is broad statistics.

## Changes

Rebuilt from definitions through actual operations. RL starts from sequential rewards, values, regression and softmax updates, then covers growing critic history, rare-switching failure, optimality targets, resets, tracking and the guarantee. DMOP starts from hidden disease states, develops particle prediction/weighting/resampling, then fixed ancestors, correction weights, derivatives, discounting and fitting.

Notation, source assumptions and qualifications are on slides. No speaker notes required. Includes original tracking, DMOP and control pipeline figures. Current manuscript title and error theorem verified against GitHub. Source map in provenance/SOURCES.md.

## Verification

Both overlay and handout builds compiled with Tectonic. Full initial handout rendered and all 58 pages visually inspected. Corrected title-page parsing, diagram widths/labels, hybrid panel clipping, current DMOP source figure, and current title. Representative overlays and final changed pages inspected before export. No overfull hbox/vbox warnings in final builds. Benign source JPEG DPI and imported PDF version warnings remain.

## Sync and next work

Source ZIP is suitable for a new Overleaf project, with XeLaTeX and main.tex selected. Preserve any subsequent live edits by downloading/comparing before next sync. Publication and live compile status are appended after delivery verification.

A rehearsal remains necessary to check the 60-minute allocation. No independent-agent review has been claimed for this new deck.

## Delivery verification

Final local exports: 131 overlay pages, 58 handout pages (48 main + 10 backup). No overfull/underfull/undefined warnings. All main pages and backups reviewed in rendered contact sheets; dense figures and final changed pages inspected separately. Representative reveals inspected for frames 16, 34, 35. Later QMDP revision replaces a text block with a branching diagram.

GitHub: source added through a clean checkout of current remote main, commit e8640ce, preserving all remote proposal edits. A follow-up commit records this status.

Overleaf: Safari reached the authenticated project list. Two CUA calls timed out on project creation; no upload or new project was verified. Existing proposal project was not changed. `output/thesis-defense-2026-source.zip` is ready for upload to a new project (XeLaTeX, main.tex). Live Overleaf compilation and GitHub linkage of that new project remain pending. Do not describe those as completed.
