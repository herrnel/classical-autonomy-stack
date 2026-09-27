from abc import ABC, abstractmethod
from observation import Observation

class Vehicle(ABC):

    @abstractmethod
    def command(self, velocity_mps: float, steering_rad: float):
        """Commands must contain velocity_mps and steering_rad"""
        pass
    
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def observe(self) -> Observation:
        pass


