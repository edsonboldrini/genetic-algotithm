import random
from ast import literal_eval

class Particle():
    bin = 0.0
    fitness = 0.0

    def __init__(self, dec):
        self.bin = self.decToBin10(dec)

    def decToBin10(self, dec):
        return (bin(dec))[2:].rjust(10, '0')

    def bin10ToDec(self):
        return float(literal_eval("0b" + str(self.bin)))

    def normalize(self):
        return (-20) + (40) * (self.bin10ToDec()/((2**10) - 1))

def main():
    X = []
    for x in range(10):
        X.append(Particle(random.randint(0, 1024)))

    for p in X:
        print(p.bin + " - " + str(p.bin10ToDec()) + " - " + str(p.normalize()))
    

if __name__ == "__main__":
    main()