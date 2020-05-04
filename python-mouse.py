import mouse
import time
while True:
    #time.sleep(180)
    time.sleep(2)
    mouse.move(100, 100, absolute=False, duration=0.5)
    mouse.move(-100, -100, absolute=False, duration=0.5)
    mouse.click('left')
