from pysimverse import Drone
import time

# 1. Initialize and connect to the simulator
drone = Drone()
drone.connect()

# 2. Basic flight commands
drone.take_off()

drone.move_forward(80)
time.sleep(1)
drone.move_backward(360)
time.sleep(1)
drone.move_left(80)
time.sleep(1)
drone.move_right(80)

time.sleep(2)

drone.land()

