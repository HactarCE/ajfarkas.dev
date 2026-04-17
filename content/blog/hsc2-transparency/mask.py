#!/usr/bin/env python3
#
# Combines a grayscale mask with an image on a black background to create a
# transparent image

from PIL import Image
from math import floor

img = Image.open("img.png")
mask = Image.open("mask.png")
pixels = img.load()
pixels_mask = mask.load()

W, H = img.size

def linear_to_gamma(linear: float) -> float:
    return max(1.055 * pow(linear, 0.416666667) - 0.055, 0.0)

def gamma_to_linear(gamma: float) -> float:
    return gamma * (gamma * (gamma * 0.305306011 + 0.682171111) + 0.012522878)

def mix(a,b,t):
    return a*(1-t)+b*t

for x in range(int(W)):
    for y in range(int(H)):
        r, g, b, _ = pixels[x, y]
        a, _, _, _ = pixels_mask[x, y]
        r, g, b, transparency = map(lambda g: gamma_to_linear(g/255), (r,g,b,a))
        div = transparency
        a = transparency

        if div==0:
            pixels[x, y] = (0,0,0,0)
        else:
            pixels[x, y] = tuple(map(lambda l: floor(linear_to_gamma(l)*255), (r/div, g/div, b/div, a)))

img.save("out.png")
