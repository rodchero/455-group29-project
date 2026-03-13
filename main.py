import random

class Individual:
    def __init__(self, schema, grid_size=100):
        self.genes = []
        self.offsets = {}
        self.fitness = 0
        
        current_index = 0
        for service, count in schema.items():
            # this is to store where each building category starts
            self.offsets[service] = current_index
            
            # randomly fill the list with coordinates
            for _ in range(count):
                self.genes.append((random.randint(0, grid_size), 
                                   random.randint(0, grid_size)))
            current_index += count

    def __repr__(self):
        return f"City(Fit: {self.fitness}, Genes: {self.genes[:3]})"

def fitnessFunction(individual):
    return "whatever fitness is calcualted for individual"

def parentSelection(pop, tournament_size=3):

    selected_parents = []
    tournament = ["individuals selected"]
    return selected_parents

def survivorSelection(pop):
    return "whatever survivors selected (we are doing offspring + parent)"

def mutate(individual):
    return "mutated individual"

def cut_crossfill(p1,p2):
    return p1,p2

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