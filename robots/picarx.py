from base import Vehicle
from picarx import Picarx
import math


class PiCarX(Vehicle):

    def __init__(self):
        px = Picarx()
    
    def command(self, velocity_mps: float, steering_rad: float):
        self.px.forward(velocity_mps)
        self.set_steering_angle(steering_rad)


    def set_steering_angle(self, steering_rad):
        steering_deg = math.degrees(steering_rad)
        sunfounder_angle = -steering_deg
        self.px.set_dir_servo_angle(sunfounder_angle)

        
