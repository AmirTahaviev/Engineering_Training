import RPi.GPIO as GPI0
GPI0.setmode(GPI0.BCM)

led = 26
GPI0.setup(led, GPI0.OUT)

phototransistor = 6

GPI0.setup(phototransistor, GPI0.IN)

while True:
    state = GPI0.input(phototransistor)
    GPI0.output(led, not state)


