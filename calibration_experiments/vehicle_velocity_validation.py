from picarx import Picarx
import time
import readchar

manual = '''
Press keys o PiCar-X!
    Press 's' to start the timer 
    Press 's' again to stop the timer
    press 'r' to restart the measurement
    ctrl+c: Quit
'''

def show_info():
    print("\033[H\033[J",end='')  # clear terminal windows
    print(manual)


if __name__ == "__main__":
    try:
        # init picarx
        px = Picarx()

        sunfounder_speed = 80

        while True:

            show_info()

            # Start Reset Timer
            start_time = time.perf_counter()

            # test motor
            px.forward(sunfounder_speed)

            while True:
                # read_key() blocks until any key is pressed, then returns its name
                key = readchar.readkey()
                key = key.lower()
                print(f"You pressed: {key}")
                
                if key == "s":
                    print("Starting Timer...")
                    break

            # Start Performance Timer
            perf_start_time = time.perf_counter()

            while True:
                # read_key() blocks until any key is pressed, then returns its name
                key = readchar.readkey()
                key = key.lower()
                print(f"You pressed: {key}")
                
                if key == "s":
                    print("Timer Stopped!")
                    break

            # End the timer
            end_time = time.perf_counter()
            px.stop()
            time.sleep(1)

            print("Time was: ", end_time - perf_start_time)
            print("Reversing...")

            px.backward(sunfounder_speed)
            time.sleep(end_time - start_time)

            px.stop()
    
            print("Reversing Stopped")
            print("Press 'r' to start another measurement or 'q' to quit")

            while True:
                key = readchar.readkey()
                key = key.lower()
                if key == 'r':
                    break
                elif key == 'q':
                    exit()


    finally:
        px.stop()
        time.sleep(0.2)


