def generate_random_solutions(solution_length):
    min = pow(2, solution_length - 1)
    max = min

    for i in range(solution_length - 1):
        max += pow(2, i)

    first_generation = []

    for i in range(min, max + 1):
        first_generation.append(generate_bin_as_str(i))

    for i in range(solution_length - 1):
        single_pick_solution = generate_bin_as_str(pow(2, i))
        single_pick_solution = "0" * (solution_length - 1 - i) + single_pick_solution

        first_generation.append(single_pick_solution)

    blank_solution = "0" * solution_length

    first_generation.append(blank_solution)

    return first_generation


def generate_bin_as_str(num):
    return str(bin(num)[2:])
