#Marjorie
#3rd last week

from pysimverse import Drone
import time
 
#mission2
# Connect to the drone and take off 
drone = Drone()
drone.connect()

drone.take_off(200)

left_right = 6
forward_backward = 10
up_down = 0
yaw = 0.1

while True:
    drone.send_rc_control(
        left_right=left_right,
        forward_backward=forward_backward,
        up_down=up_down,
        yaw=yaw
    )