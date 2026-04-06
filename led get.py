import RPi.GPIO as GPI0
import time

GPI0.setmode(GPI0.BCM)

led = 26
GPI0.setup(led, GPI0.OUT)
state = 0 
period = 1.0

while True:
    GPI0.output(led, state)
    time.sleep(period)
    state = not state 
