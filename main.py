from city import *
from individual import *
from ea import *

POP_SIZE = 2
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.1

def main():

    # urban_blueprint = {
    #     'school': 2,
    #     'emergency': 3,
    #     'grocery': 4
    # }

    urban_blueprint = {
        'school': 1,
        'emergency': 2,
    }
    
    ea = EA(POP_SIZE, NUM_GENERATIONS, MUTATION_RATE, urban_blueprint, City(seed=42))

    print(City(seed=42))

    print("Initial Population:")
    print(ea.population)

    ea.visualize_population(2)
    

if __name__ == "__main__":
    main()