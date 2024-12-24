def generate_random_solutions(solution_length):
    min = pow(2, solution_length - 1)
    max = min

    for i in range(solution_length - 1):
        max += pow(2, i)

    random_solutions = []

    for i in range(min, max):
        random_solutions.append(generate_bin_as_str(i))

    for i in range(solution_length - 1):
        single_pick_solution = generate_bin_as_str(pow(2, i))
        single_pick_solution = "0" * (solution_length - 1 - i) + single_pick_solution

        random_solutions.append(single_pick_solution)

    blank_solution = "0" * solution_length

    random_solutions.append(blank_solution)

    return random_solutions


def generate_bin_as_str(num):
    return str(bin(num)[2:])
