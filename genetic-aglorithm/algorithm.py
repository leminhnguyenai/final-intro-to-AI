import utils
import random


class Genetic_algorithm:
    def __init__(self, weights_list, prices_list, max_capacity):
        self.weights_list = weights_list
        self.prices_list = prices_list
        self.max_capacity = max_capacity

        solution_length = len(weights_list)

        self.population = utils.generate_random_solutions(solution_length)

    def run(self, cycle_num):
        if cycle_num == 0:
            self.ranking()
            final_best_solution = self.population[len(self.population) - 1]
            final_best_fitness_score = self.fitness(final_best_solution)

            print(f"{final_best_fitness_score} {final_best_solution}")
            return final_best_fitness_score, final_best_solution

        self.ranking()
        self.generate_new_generation()

        current_best_solution = self.population[len(self.population) - 1]
        current_best_fitness_score = self.fitness(current_best_solution)

        if self.is_converged(current_best_solution):
            print(f"{current_best_fitness_score} {current_best_solution}")
            return current_best_fitness_score, current_best_solution

        return self.run(cycle_num - 1)

    def ranking(self):
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

        def is_valid_solution(solution):
            return self.fitness(solution) != -1

        filtered_population = filter(is_valid_solution, self.population)
        self.population = list(filtered_population)

    def generate_new_generation(self):
        # Initiate new population with 2 highest solution first
        current_population_length = len(self.population)

        current_solution_dad = self.population[current_population_length - 1]
        current_solution_mom = self.population[current_population_length - 2]
        new_population = [current_solution_dad, current_solution_mom]

        while current_population_length > 1:
            current_population_length -= 2

            current_solution_dad = self.population[current_population_length - 1]
            current_solution_mom = self.population[current_population_length - 2]

            new_child_solution_1, new_child_solution_2 = self.crossover(
                current_solution_dad, current_solution_mom
            )

            new_population.append(new_child_solution_1)
            new_population.append(new_child_solution_2)

        self.population = new_population

    def fitness(self, solution):
        current_capacity = 0
        current_price = 0
        items_count = len(self.weights_list)

        for i in range(items_count):
            is_included = int(solution[i])
            if is_included == 0:
                continue
            current_capacity += self.weights_list[i]
            current_price += self.prices_list[i]

        if current_capacity > self.max_capacity:
            return -1

        return current_price

    def crossover(self, solution_mom, solution_dad):
        random_pos_to_cut = random.randint(1, len(solution_dad) - 2)

        dad_dominant_gene = solution_dad[:random_pos_to_cut]
        dad_recessive_gene = solution_dad[random_pos_to_cut:]
        mom_dominant_gene = solution_mom[:random_pos_to_cut]
        mom_recessive_gene = solution_mom[random_pos_to_cut:]

        new_child_solution_1 = dad_dominant_gene + mom_recessive_gene
        new_child_solution_2 = mom_dominant_gene + dad_recessive_gene

        return new_child_solution_1, new_child_solution_2

    def mutate(self, solution):
        random_gene_to_mutate_index = random.randint(0, len(solution) - 1)

        solution_as_array = list(solution)

        gene_to_be_mutated_as_int = int(solution_as_array[random_gene_to_mutate_index])
        gene_to_be_mutated_as_int += 1
        gene_to_be_mutated_as_int %= 2

        solution_as_array[random_gene_to_mutate_index] = str(gene_to_be_mutated_as_int)

        mutated_solution = "".join(solution_as_array)

        return mutated_solution

    # Function to check if the algorithm reach convergence or not
    def is_converged(self, best_solution):
        best_solution_as_array = list(best_solution)

        for i in range(len(best_solution_as_array)):
            gene = int(best_solution_as_array[i])
            if gene == 0:
                better_solution_as_array = best_solution_as_array.copy()
                # Add 1 more object to the bag and check if the fitness score is valid or not
                better_solution_as_array[i] = "1"
                better_solution = "".join(better_solution_as_array)
                if self.fitness(better_solution) != -1:
                    return False

        return True
