from controller import Robot, Keyboard, Motion

timestep = 32
robot = Robot()
keyboard = Keyboard()
keyboard.enable(timestep)
wave = Motion("../../motions/wave.motion")

def printMessages():
    print("Press up arrow to wave!")
    key = -1

printMessages()

            
while robot.step(timestep) != -1:
    key = keyboard.getKey()
    if key == keyboard.UP:
        wave.play()
