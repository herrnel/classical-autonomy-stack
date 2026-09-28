---
step: 1
date: "2025 · Step 01"
title: "Defining the Vehicle interface"
tag: "base/"
image: "timeline/step-1.svg"
summary: "An abstract Vehicle contract — command(), stop(), observe() — plus an Observation data model."
---

I wanted to start from the smallest possible contract instead of a hardware
SDK. If I could describe a robot as just three verbs — command it, stop it,
observe it — then every planner and controller I write later stays honest and
portable.

### The contract

`base/vehicle.py`

```python
from abc import ABC, abstractmethod
from observation import Observation

class Vehicle(ABC):
    @abstractmethod
    def command(self, velocity_mps: float, steering_rad: float):
        """Commands must contain velocity_mps and steering_rad"""

    @abstractmethod
    def stop(self): ...

    @abstractmethod
    def observe(self) -> Observation: ...
```

Observation was the harder call: I kept it to a camera image, a front range
reading and a timestamp. No premature fields. It felt slow to write so little,
but this is the seam the rest of the project hangs on.

`base/observation.py`

```python
class Observation:
    def __init__(self, image, front_range_m, timestamp):
        self.__image = image
        self.__front_range_m = front_range_m
        self.__timestamp = timestamp
```
