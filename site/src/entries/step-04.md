---
step: 4
date: "2025 · Step 04"
title: "Calibrating steering"
tag: "calibration_experiments/"
image: "timeline/step-4.svg"
summary: "Mapping servo angle to an actual steering radius so a commanded turn matches reality."
---

Steering was subtler than velocity because the error compounds over a path, not
a point. A few degrees of servo bias becomes a slow drift into the wall.

![Measured arc vs. commanded servo angle.](/classical-autonomy-stack/timeline/plot-steering.svg)
*Measured arc vs. commanded servo angle (dashed = ideal linear response).*

I built a small validation script and watched the difference between what I
asked for and what the geometry did. Getting this repeatable — same command,
same arc — mattered more to me than getting it perfectly centred.
