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
    
    print("INITIALIZING...")
    city = City(seed=42)
    ea = EA(POP_SIZE, NUM_GENERATIONS, MUTATION_RATE, urban_blueprint, city)

    ea.population[0].genes = [
        (0,1),
        (1,0),
        (1,1)
    ]

    ea.population[1].genes = [
        (2,1),
        (2,0),
        (2,2)
    ]

    print("STARTING EVOLUTION...")
    ea.run()
    

if __name__ == "__main__":
    main()