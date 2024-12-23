import utils
import random


class Genetic_algorithm:
    def __init__(self, weights_list, prices_list, max_capacity):
        self.weights_list = weights_list
        self.prices_list = prices_list
        self.max_capacity = max_capacity

        solution_length = len(weights_list)

        self.population = utils.generate_random_solutions(solution_length)

    def run(self):
        for solution in self.population:
            print(solution)
            solution = self.mutate(solution)
            print(solution)
            print("")

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

    def mutate(self, solution):
        random_gene_to_mutate_index = random.randint(0, len(solution) - 1)

        solution_as_array = list(solution)

        gene_to_be_mutated = int(solution_as_array[random_gene_to_mutate_index])
        gene_to_be_mutated += 1
        gene_to_be_mutated %= 2

        solution_as_array[random_gene_to_mutate_index] = str(gene_to_be_mutated)

        mutated_solution = "".join(solution_as_array)

        return mutated_solution
