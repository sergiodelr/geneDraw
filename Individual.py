import numpy as np
import random
from PIL import Image, ImageFont, ImageDraw
from Algorithm import Algorithm
import math

class Individual:

    def __init__(self, dimX, dimY):
        self.chromoSize = 700
        self.chromo = np.empty(self.chromoSize, int)
        self.fitness = 0
        self.dimY = dimY
        self.dimX = dimX

        for i in range(0, self.chromoSize, 7):
            self.chromo[i] = random.randint(0, dimX - 1)  # ellipse left limit
            self.chromo[i + 1] = random.randint(0, dimY - 1)  # ellipse top limit
            self.chromo[i + 2] = random.randint(self.chromo[i] + 1, dimX)  # ellipse right limit
            self.chromo[i + 3] = random.randint(self.chromo[i + 1] + 1, dimY)  # ellipse bottom limit
            self.chromo[i + 4] = random.randint(0, 255)  # red
            self.chromo[i + 5] = random.randint(0, 255)  # green
            self.chromo[i + 6] = random.randint(0, 255)  # blue

    def fitnessCalc(self):
        img = Image.new("RGB", (self.dimX, self.dimY))
        draw = ImageDraw.Draw(img)

        for i in range(0, self.chromoSize, 7):
            draw.ellipse((self.chromo[i], self.chromo[i + 1], self.chromo[i + 2], self.chromo[i + 3]),
                         (self.chromo[i + 4], self.chromo[i + 5], self.chromo[i + 6]))
        sumR, sumG, sumB = 0, 0, 0
        pixelSum = 0
        px = list(img.load().getdata())
        pxOrig = list(Algorithm.pxImage.getdata())
        for i in range(len(px)):
            sumR += (px[i][0] - pxOrig[i][0]) ** 2
            sumG += (px[i][1] - pxOrig[i][1]) ** 2
            sumB += (px[i][2] - pxOrig[i][2]) ** 2
            pixelSum = math.sqrt(sumB + sumR + sumG)
            self.fitness += pixelSum
        self.fitness = -1/math.log1p(self.fitness + 1)
