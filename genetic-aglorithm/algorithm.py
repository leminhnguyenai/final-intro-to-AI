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
        self.selection()

    def selection(self):
        prev_population_count = len(self.population)

        for final in range(prev_population_count, 1, -1):
            for i in range(final - 1):
                if self.fitness(self.population[i]) <= self.fitness(
                    self.population[i + 1]
                ):
                    continue

                swap = self.population[i]
                self.population[i] = self.population[i + 1]
                self.population[i + 1] = swap

        print(self.population[len(self.population) - 1])
        print(self.population[len(self.population) - 2])

    def fitness(self, solution):
        current_capacity = 0
        items_count = len(self.weights_list)

        for i in range(items_count):
            is_included = int(solution[i])
            if is_included == 1:
                continue
            current_capacity += self.weights_list[i] * self.prices_list[i]

        if current_capacity > self.max_capacity:
            return -1

        return current_capacity

    def mutate(self, solution):
        random_gene_to_mutate_index = random.randint(0, len(solution) - 1)

        solution_as_array = list(solution)

        gene_to_be_mutated_as_int = int(solution_as_array[random_gene_to_mutate_index])
        gene_to_be_mutated_as_int += 1
        gene_to_be_mutated_as_int %= 2

        solution_as_array[random_gene_to_mutate_index] = str(gene_to_be_mutated_as_int)

        mutated_solution = "".join(solution_as_array)

        return mutated_solution

    def crossover(self, solution_mom, solution_dad):
        random_pos_to_cut = random.randint(1, len(solution_dad) - 2)

        dad_dominant_gene = solution_dad[:random_pos_to_cut]
        dad_recessive_gene = solution_dad[random_pos_to_cut + 1 :]
        mom_dominant_gene = solution_mom[:random_pos_to_cut]
        mom_recessive_gene = solution_mom[random_pos_to_cut + 1 :]

        new_child_solution_1 = dad_dominant_gene + mom_recessive_gene
        new_child_solution_2 = mom_dominant_gene + dad_recessive_gene

        return new_child_solution_1, new_child_solution_2
