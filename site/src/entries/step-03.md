---
step: 3
date: "2025 · Step 03"
title: "Calibrating velocity"
tag: "calibration_experiments/"
image: "timeline/step-3.svg"
summary: "A bench experiment mapping commanded motor speed to real-world metres per second."
---

Nothing humbles you like a tape measure. I commanded fixed speeds, timed the
car over a known distance, and the numbers were not linear the way I'd hoped.

![Commanded speed vs. measured m/s.](/classical-autonomy-stack/timeline/plot-velocity.svg)
*Commanded speed vs. measured m/s — clearly non-linear at the low end.*

I stopped trying to derive the mapping and just measured it. This entry is
really about a mindset shift: the code is only as trustworthy as the last time
I validated it against the floor of my apartment.
