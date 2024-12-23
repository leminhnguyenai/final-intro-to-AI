import utils


class Genetic_algorithm:
    def __init__(self, weights_list, prices_list, max_capacity):
        self.weights_list = weights_list
        self.prices_list = prices_list
        self.max_capacity = max_capacity

        solution_length = len(weights_list)

        self.population = utils.generate_random_solutions(solution_length)

    def run(self):
        for solution in self.population:
            print(self.fitness(solution))

    def fitness(self, solution):
        current_capacity = 0
        items_count = len(self.weights_list)

        for i in range(items_count):
            is_included = int(solution[i])
            if is_included == 0:
                continue
            current_capacity += self.weights_list[i] * self.prices_list[i]

        if current_capacity > self.max_capacity:
            return -1

        return current_capacity
