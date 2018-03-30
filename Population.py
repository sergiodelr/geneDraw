import numpy as np
from Individual import Individual


class Population:

    def __init__(self, size, dimX, dimY, initialize):
        if initialize:
            self.individuals = [Individual(dimX, dimY) for _ in range(size)]
        self.size = size
        self.fittest = None

    def getFittest(self):
        if self.fittest is None:
            for i in range(self.size):
                self.individuals[i].fitnessCalc()
            self.fittest = self.individuals[0]
            for ind in self.individuals:
                self.fittest = self.fittest if self.fittest.fitness > ind.fitness else ind
        return self.fittest
