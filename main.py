from city import *
from individual import *
from ea import *


def main():

    urban_blueprint = {
        'school': 2,
        'emergency': 3,
        'grocery': 4
    }
    
    # population generation
    population = [Individual(urban_blueprint) for _ in range(10)]

    print("Initial Population:")
    print(population)
    

if __name__ == "__main__":
    main()