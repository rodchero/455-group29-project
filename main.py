from city import *
from individual import *
from ea import *

POP_SIZE = 20
NUM_GENERATIONS = 10000
MUTATION_RATE = 0.5

def main():

    urban_blueprint = {
        'school': 8,
        'emergency': 3,
        'grocery': 2
    }

    # urban_blueprint = {
    #     'school': 2,
    #     'emergency': 1,
    # }
    
    print("INITIALIZING...")
    city = City((20, 20), seed=45)
    ea = EA(POP_SIZE, NUM_GENERATIONS, MUTATION_RATE, urban_blueprint, city)

    print("STARTING EVOLUTION...")
    ea.run()
    

if __name__ == "__main__":
    main()