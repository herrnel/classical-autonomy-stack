from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        # init picarx
        px = Picarx()

        px.set_dir_servo_angle(0)
        time.sleep(20)

        # test direction servo
        px.set_dir_servo_angle(-10)
        time.sleep(0.01)
    finally:
        px.stop()
        time.sleep(0.2)


