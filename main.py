from city import *
from individual import *
from ea import *

POP_SIZE = 30
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.5

def main():

    urban_blueprint = {
        'school': 11,
        'emergency': 6,
        'grocery': 5
    }

    # urban_blueprint = {
    #     'school': 2,
    #     'emergency': 1,
    # }
    
    print("INITIALIZING...")
    city = City((50, 50), seed=49)
    ea = EA(POP_SIZE, NUM_GENERATIONS, MUTATION_RATE, urban_blueprint, city)

    print("STARTING EVOLUTION...")
    ea.run()
    ea.plot_convergence() 
    

if __name__ == "__main__":
    main()