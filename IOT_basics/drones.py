import pysimverse
import time

print("Attempting to open drone window...")

# Try to start the simulation
# (Note: use whatever startup command your specific tutorial gave you)
sim = pysimverse.make("Drone-v0") 
sim.reset()

print("If you see this, the code is still running!")
input("STOP! Look for the window now. Press ENTER here to finally close it.")
