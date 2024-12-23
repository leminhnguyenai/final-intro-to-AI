def generate_random_solutions(solution_length):
    min = pow(2, solution_length - 1)
    max = min

    for i in range(solution_length - 1):
        max = max + pow(2, i)

    random_solutions = []

    for i in range(min, max):
        random_solutions.append(str(bin(i)[2:]))

    return random_solutions
