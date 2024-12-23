import utils


class Genetic_algorithm:
    def __init__(self, weights_list, prices_list, capacity):
        self.weights_list = weights_list
        self.prices_list = prices_list
        self.capacity = capacity

        solution_length = len(weights_list)

        self.population = utils.generate_random_solutions(solution_length)
