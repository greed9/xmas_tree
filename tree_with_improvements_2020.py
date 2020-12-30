# Circuit Playground NeoPixel
import time
import board
import neopixel
import random

NUM_PIXELS = 45
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(board.A6, 46, brightness=0.2, auto_write=False)
cpx_pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

# Star at top
class Star:

    def __init__(self, color):
        self.color = color
        self.counter = 0
        self.effect = None

    def set_color(self, color):
        self.color = color
        for i in range(0, 10):
            cpx_pixels[i] = color
        cpx_pixels.show()

    def blink(self, wait):
        self.effect = self.blink
        cpx_pixels[self.counter] = self.color
        time.sleep(0.1)
        cpx_pixels[self.counter] = OFF
        cpx_pixels.show()

    def step(self):
        self.counter += 1
        self.effect(self.color)
        if self.counter > 7:
            self.counter = 0

# Represents one tier of the tree
class Tier:

    def __init__(self, color, start_pixel, num_pixels):
        self.start_pixel = start_pixel
        self.num_pixels = num_pixels
        self.color = color
        self.effect = None
        self.counter = start_pixel
        self.target_pixel = -1
        self.remembered_color = OFF

    def stop(self):
        self.counter = 0

    def step(self):
        self.counter += 1
        self.effect(self.color)

    def blink(self, color):
        if self.target_pixel != -1:
            pixels[self.target_pixel] = self.remembered_color

        target_pixel = random.randrange(self.start_pixel, self.start_pixel + self.num_pixels, 1 )
        self.remembered_color = pixels[target_pixel]
        pixels[target_pixel] = color
        self.target_pixel = target_pixel

    def tier_color(self, color):
        self.effect = self.tier_color
        if self.counter < self.start_pixel + self.num_pixels:
            pixels[self.counter] = color
            pixels.show()
        else:
            self.counter = self.start_pixel

tier1 = Tier(BLUE, 0, 6)
tier2 = Tier(WHITE, 6, 7)
tier3 = Tier(GREEN, 13, 14)
tier4 = Tier(RED, 27, 19)

theStar = Star(YELLOW)

def color_tree(color):
    pixels.fill(color)
    pixels.show()

def sparkle_tree(color, reps, wait):
    for i in range(0, reps):
        target_pixel = random.randrange(0, NUM_PIXELS, 1)
        save_pixel = pixels[target_pixel]
        pixels[target_pixel] = color
        pixels.show()
        time.sleep(wait)
        pixels[target_pixel] = save_pixel
        pixels.show()

def blink_tree(color):
    tier1.blink(color)
    tier2.blink(color)
    tier3.blink(color)
    tier4.blink(color)


    tier1.step()

    time.sleep(0.0)
    tier2.step()

    time.sleep(0.0)
    tier3.step()

    time.sleep(0.0)
    tier4.step()

    tier4.step()
    tier4.step()
    tier4.step()

    tier4.step()
    time.sleep(0.0)

def fill_tree(wait, color):
    tier1.tier_color(color)
    tier2.tier_color(color)
    tier3.tier_color(color)
    tier4.tier_color(color)

    tier1.step()
    time.sleep(0.0)
    tier2.step()
    time.sleep(0.0)
    tier3.step()
    time.sleep(0.0)
    tier4.step()
    time.sleep(0.0)

def main():
    print( 'tree_with_improvements_2020.py')
    while(True):
        cpx_pixels.fill(OFF)
        pixels.fill(OFF)

        theStar.set_color(YELLOW)

        # color_tree(GREEN)

        print('fill_tree(green)')
        for i in range(0, NUM_PIXELS):
            fill_tree(0, GREEN)

        time.sleep(0.5)

        print('blink_tree(OFF)')
        for i in range(0, 100):
            blink_tree(OFF)

        pixels.fill(OFF)
        pixels.show()

        print('blink_tree(WHITE)')
        for i in range(0, 100):
            blink_tree(WHITE)

        pixels.fill(OFF)
        pixels.show()
        time.sleep(0.5)

        print('color_tree(BLUE)')
        color_tree(BLUE)
        time.sleep(2.0)

        print('sparkle_tree(WHITE)')
        sparkle_tree(WHITE, 100, 0.05)
        time.sleep(2.0)

        print('color_tree(WHITE)')
        color_tree(WHITE)
        time.sleep(1.0)
        print('sparkle_tree(BLUE)')
        sparkle_tree(BLUE, 100, 0.07)

        time.sleep(2.0)

        print( 'color_tree(RED)')
        color_tree(RED)
        time.sleep(2.0)
        print('sparkle_tree(WHITE)')
        sparkle_tree(WHITE, 100, 0.07)

        time.sleep(2.0)

        print('color_tree(WHITE)')
        color_tree(WHITE)
        time.sleep(2.0)
        print('sparkle_tree(RED)')
        sparkle_tree(RED, 100, 0.07)

        time.sleep(2)

        print( 'color_tree(GREEN)')
        color_tree(GREEN)
        time.sleep(2.0)
        print('sparkle_tree()')
        sparkle_tree(WHITE, 100, 0.07)

        time.sleep(2.0)

        print('color_tree(WHITE)')
        color_tree(WHITE)
        time.sleep(2.0)
        print('sparkle_tree()')
        sparkle_tree(GREEN, 100, 0.07)

        time.sleep(2.0)
if __name__ == "__main__":
    main()