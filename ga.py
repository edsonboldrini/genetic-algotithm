import random
import math
import random
import copy


from ast import literal_eval

POPULATION_SIZE = 10
GENERATIONS_NUMBER = 10
MIN_VALUE = -20
MAX_VALUE = 20
BITS_LENGTH = 10
TOURNAMENT_NUMBER = 2
TAXA_MUTACAO = 0.05

class Particle:
    bin = ''
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

    def crossover(self, outro):
        cut_point = BITS_LENGTH//2

#        print('pai1 bin = ' + self.bin + ' pai2 bin = ' + outro.bin)

        self_1_part = self.bin[0:cut_point]
        self_2_part = self.bin[cut_point:BITS_LENGTH]
        outro_1_part = outro.bin[0:cut_point]
        outro_2_part = outro.bin[cut_point:BITS_LENGTH]

#        print('pai1 1 parte = ' + self_1_part + ' pai1 2 parte = ' + self_2_part)
#        print('pai2 1 parte = ' + outro_1_part + ' pai2 2 parte = ' + outro_2_part)

        self.bin = self_1_part + outro_2_part
        outro.bin = outro_1_part + self_2_part

    def mutacao(self):
        bin_list = list(self.bin)
        for i in range(len(bin_list)):
            if random.uniform(0.0, 1.0) <= TAXA_MUTACAO:

                if bin_list[i] == '0':
                    bin_list[i] = '1'
                elif bin_list[i] == '1':
                    bin_list[i] = '0'
        self.bin = ''.join(bin_list)

def main():
    pai_elite = None
    population = []
    for individual in range(POPULATION_SIZE):
        population.append(Particle(random.randint(0, 1024)))
    population.sort(key=lambda x: x.fitness)
    pai_elite = copy.copy(population[0])

    contador_geracao = 0
    while contador_geracao < GENERATIONS_NUMBER:
        contador_geracao += 1

        for individual in population:
            individual.calcFitness()
        population.sort(key=lambda x: x.fitness)

        population_new = []
        while len(population_new) < POPULATION_SIZE:
            #Selecionando os dois pais para realizar o crossover
            pai1 = None
            pai2 = None

            tournament_participants = []
            for indice_tournament in range(TOURNAMENT_NUMBER):
                tournament_participants.append(population[random.randint(0, POPULATION_SIZE-1)])
            tournament_participants.sort(key=lambda x: x.fitness)
            pai1 = tournament_participants[0]

            tournament_participants = []
            for indice_tournament in range(TOURNAMENT_NUMBER):
                tournament_participants.append(population[random.randint(0, POPULATION_SIZE-1)])
            tournament_participants.sort(key=lambda x: x.fitness)
            pai2 = tournament_participants[0]

            pai1.crossover(pai2)
            pai1.mutacao()
            pai2.mutacao()
            population_new.append(pai1)
            population_new.append(pai2)

        population_new.sort(key=lambda x: x.fitness, reverse=True)
        if (pai_elite.fitness < population_new[0].fitness):
            population_new[0] = copy.copy(pai_elite)

        population = population_new
        population.sort(key=lambda x: x.fitness, reverse=True)
        pai_elite = copy.copy(population[0])

        for p in population_new:
            print(p.fitness)
        population_new.sort(key=lambda x: x.fitness)

        print("\n BEST OF GENERATION = " + str(population_new[0].fitness))




    #for individual in population:
     # print(individual.bin + " - " + str(individual.bin10ToDec()) + " - " + str(individual.normalize()) + " Fitness = " + str(individual.fitness))
    #print("best value = " + best.fitness + "of x value = " + best.normalize())


if __name__ == "__main__":
    main()