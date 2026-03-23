# Marjorie
# 3rd last week

from pysimverse import Drone
import time
impoort time


#mission 1
drone = Drone()
drone.connect()

drone.take_off(100)



drone.move_forward(250)
drone.move_right(250)

drone.land()