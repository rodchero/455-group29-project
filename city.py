import random as rng

'''Class which represents the city as a grid with population distribution.'''
class City:
    def __init__(self, grid_size=(10, 10), population_range=(0, 10), seed = 0):
        self.population_distribution = []
        self.grid_size = grid_size
        self.min_population = population_range[0]
        self.max_population = population_range[1]

        # to allow for reproducibility 
        rng.seed(seed)

        for _ in range(grid_size[1]):
            # TODO: This should really be perlin noise (instead of white noise) for more realistic-looking population densities
            row = [rng.randint(self.min_population, self.max_population) for _ in range(grid_size[0])]
            self.population_distribution.append(row)
        
        return


    def __repr__(self):
        res=""
        res+= "===="*self.grid_size[0] + "=\n"
        for row in self.population_distribution:
            for cell in row:
                res+=f"|{cell:3}"
            res+= "|\n" + "----"*self.grid_size[0] + "-\n" 
        res+= "===="*self.grid_size[0] + "=\n" 
        return res
    

if __name__ == "__main__":
    print("Example city with seed=42")
    print(City(grid_size=(10, 10), seed=42))