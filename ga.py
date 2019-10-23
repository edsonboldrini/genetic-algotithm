import random
import math
import random

from ast import literal_eval

POPULATION_SIZE = 10
GENERATIONS_NUMBER = 10
MIN_VALUE = -20
MAX_VALUE = 20
BITS_LENGTH = 10
TOURNAMENT_NUMBER = 2

class Particle:
    bin = 0.0
    fitness = 0.0

    def __init__(self, dec):
        self.bin = self.decToBin10(dec)

    def decToBin10(self, dec):
        return (bin(dec))[2:].rjust(10, '0')

    def bin10ToDec(self):
        return float(literal_eval("0b" + str(self.bin)))

    def normalize(self):
        return MIN_VALUE + (MAX_VALUE-MIN_VALUE) * (self.bin10ToDec()/((2**BITS_LENGTH) - 1))

    def calcFitness(self):
        self.fitness = math.cos(self.normalize())*self.normalize()+2



def main():
    best = None
    population = []
    for individual in range(POPULATION_SIZE):
        population.append(Particle(random.randint(0, 1024)))

    contador_geracao = 0
    while contador_geracao < GENERATIONS_NUMBER:

        for individual in population:
            individual.calcFitness()
        population.sort(key=lambda x: x.fitness)
        best = population[0]

        contador_geracao += 1
        population_new = []
        for indice_population in range(POPULATION_SIZE):
            tournament_participants = []
            for indice_tournament in range(TOURNAMENT_NUMBER):
                tournament_participants.append(population[random.randint(0, POPULATION_SIZE)])
            tournament_participants.sort(key=lambda x: x.fitness)
            population_new.append(tournament_participants[0])




    for individual in population:
        print(individual.bin + " - " + str(individual.bin10ToDec()) + " - " + str(individual.normalize()) + " Fitness = " + str(individual.fitness))
    print("best value = " + best.fitness + "of x value = " + best.normalize())


if __name__ == "__main__":
    main()