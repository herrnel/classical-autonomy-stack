---
step: 2
date: "2025 · Step 02"
title: "The PiCar-X driver"
tag: "robots/"
image: "timeline/step-2.svg"
summary: "A concrete adapter turning velocity + steering-angle commands into SunFounder servo and motor calls."
---

This is where the abstraction met a real, noisy machine. The PiCar-X thinks in
servo values and motor duty cycles; my interface speaks m/s and radians.

### Translating units at the edge

`robots/picarx.py`

```python
class PiCarX(Vehicle):
    def command(self, velocity_mps, steering_rad):
        self.px.forward(velocity_mps)
        self.set_steering_angle(steering_rad)

    def set_steering_angle(self, steering_rad):
        steering_deg = math.degrees(steering_rad)
        sunfounder_angle = -steering_deg          # sign flip
        self.px.set_dir_servo_angle(sunfounder_angle)
```

I resisted the urge to 'fix' the vendor library and instead wrote a thin
translation layer, so the mess stays quarantined in one file and the rest of
the stack never sees it.

![PiCar-X on the bench during driver bring-up.](/classical-autonomy-stack/timeline/step-2.svg)
*PiCar-X on the bench during driver bring-up.*
