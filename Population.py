import numpy as np
from Individual import Individual


class Population:

    def __init__(self, size, dimX, dimY, initialize):
        if initialize:
            self.individuals = [Individual(dimX, dimY) for _ in range(size)]
        self.fittestScore = 0
        self.size = size

    def getFittest(self):
        for i in range(self.size):
            self.individuals[i].fitnessCalc()

