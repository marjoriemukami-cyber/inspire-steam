from robodk.robolink import

#Connect to Robodk
RDK = Robolink()

#Get robot
robot = RDK.Item('', ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("robot not found")

#Get targets 
home = RDK.Item('T1')
T1 = RDK.Item('T2')  
T4 = RDK.Item('T3')

#Check that all targets exist
if not home.Valid():
    raise Exceptions("Check that all targets are existing")

#Get Speed
robot.setSpeed(100)         #linear speed m/s
robot.setSpeedJoints(50)    #joint speed deg/s

#Move sequence
    
print("Moving to home")
robot.Move3(T1)

print("Moving to T1")
robot.Move3(T1)

print("Moving to T2")
robot.Move3(T1)

print("Moving to T3")
robot.Move3(T1)