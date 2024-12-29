import algorithm
import os


dirname = os.path.dirname(__file__)
dataset_path = os.path.join(dirname, "../dataset.csv")
output_path = os.path.join(dirname, "../output.csv")

dataset = open(dataset_path)

inputs = dataset.read().split("\n")[1:]
inputs = inputs[: len(inputs) - 2]

output = "Weights,Prices,Capacity,Best pick,Best price\n"

for input in inputs:
    agruments = input.split(",")

    weights_list_as_str = agruments[0]
    prices_list_as_str = agruments[1]
    capacity_as_str = agruments[2]

    weights_list_as_str = weights_list_as_str.replace("[", "")
    weights_list_as_str = weights_list_as_str.replace("]", "")
    prices_list_as_str = prices_list_as_str.replace("[", "")
    prices_list_as_str = prices_list_as_str.replace("]", "")

    weights_list_as_str = weights_list_as_str.split(" ")
    prices_list_as_str = prices_list_as_str.split(" ")

    def not_blankspace(str):
        return str != ""

    weights_list_as_str = list(filter(not_blankspace, weights_list_as_str))
    prices_list_as_str = list(filter(not_blankspace, prices_list_as_str))

    weights_list = []
    prices_list = []
    capacity = int(capacity_as_str)

    for i in range(len(weights_list_as_str)):
        weights_list.append(int(weights_list_as_str[i]))
        prices_list.append(int(prices_list_as_str[i]))

    alg = algorithm.Genetic_algorithm(weights_list, prices_list, capacity)

    fitness_score, solution = alg.run(100000000000)

    solution_as_arr = list(solution)

    solution_as_str = str(solution_as_arr)
    solution_as_str = solution_as_str.replace(",", "")
    solution_as_str = solution_as_str.replace("'", "")

    output += (
        agruments[0]
        + ","
        + agruments[1]
        + ","
        + agruments[2]
        + ","
        + solution_as_str
        + ","
        + str(fitness_score)
        + "\n"
    )

print(output)

f = open(output_path, "w")
f.write(output)
f.close()
