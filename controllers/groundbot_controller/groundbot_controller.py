
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

sensor = robot.getDevice("front_sensor")
sensor.enable(timestep)

laser = robot.getDevice("laser")
laser.set(0)

print("🤖 GroundBot active and moving...")

while robot.step(timestep) != -1:
    distance = sensor.getValue()
    if distance < 500:
        print("🎯 Target detected! 🔥 Laser fired!")
        laser.set(1)
    else:
        laser.set(0)
