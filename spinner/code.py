import time

from adafruit_circuitplayground.express import cpx


cpx.pixels.brightness = 0.1

COLOR = {True: (0, 0, 0xff), False: (0, 0x70, 0)}

while True:
    for i in range(10):
        forward = -1 if cpx.button_a else 1
        v = COLOR[(time.monotonic() * 10 + forward * i) % 10 < 3]
        cpx.pixels[i] = v
