import RPi.GPIO as GPI0
import time

GPI0.setmode(GPI0.BCM)
led = 26
GPI0.setup(led, GPI0.OUT)

pmw = GPI0.PWM(led, 200)
duty = 0.0
pmw.start(duty)

while True:
    pmw.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0