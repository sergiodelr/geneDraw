import numpy as np
from PIL import Image, ImageFont, ImageDraw
import colorsys
from Population import Population
from Algorithm import Algorithm
import Individual

def main():
    testImg = Image.open("test.jpg")
    dimX, dimY = testImg.size
    Algorithm.pxImage = testImg.getdata()
    testImg.close()

    generationNo = 0
    popSize = 100

    p = Population(popSize, dimX, dimY, True)
    fit = p.getFittest()
    print(fit.fitness)

    fit.draw()

if __name__ == '__main__':
    main()
