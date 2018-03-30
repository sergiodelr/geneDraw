import numpy as np
from PIL import Image, ImageFont, ImageDraw
import colorsys
from Population import Population
from Algorithm import Algorithm


def main():
    testImg = Image.open("test.jpg")
    dimX, dimY = testImg.size
    Algorithm.pxImage = testImg.load()
    testImg.close()

    generationNo = 0
    popSize = 100


    print(dimX, dimY)
    p = Population(popSize, dimX, dimY, True)
    p.getFittest()

if __name__ == '__main__':
    main()
