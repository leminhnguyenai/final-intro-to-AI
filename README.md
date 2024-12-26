> [!NOTE]
> [A Complete Guide to Genetic Algorithm — Advantages, Limitations & More](https://medium.com/@byanalytixlabs/a-complete-guide-to-genetic-algorithm-advantages-limitations-more-738e87427dbb)


# What is genetic algorithm 

- Genetic Algorithms are heuristic search algorithms that solve constrained and unconstrained optimization problems using the concepts of natural selection

- Concepts to grasp in order to understand Genetic algorithm:
    - Natural selection
    - Survival of the fittest
    - Mutation
    - Crossover
    ...

- Through genetic mutation, certain species adapt better to the surroundings

- Under natural selection, from a population, only the fittest individuals survive or are allowed by the laws of nature to produce offspring (i.e., survival of the fittest).

- The next generation due to better gene will:
    - Have beter survival rate than their parents
    - Increase there chance of producing offsprings

- The new offsprings are are often the combination of 2 different gene (crossover)

- This process keep going iterative -> at the end the population consist of the fittest of the individuals

- In each iteration, the "solution" is tweaked, the ones those perform the best are kept, the rest are discarded

# Key terminology

## Population
- Refers to the subset of all possible solutions to a problem

## Chromosome (solution)
- An individual solution is a chromosomes
- A chromosome is a finite-length vector of variable components

## Gene
- Each variable component is referred to as a gene
- A collection of genes form a chromosome

![Relation between gene, chromosome and population](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*JJ0vjBxiueGKvsBO.jpg)
- *Genes form chromosome -> Chromosomes form Population*

## Selection
- A stage where the optimal solution is selected for the next iteration for breeding

## Crossover
- Recombination of genetic information to generate new solutions

## Mutation
- Mutation's goal is to maintain diversity in a population
- Mutation is the process of randomly editing certain solution

## Allele
- The value provided by a gene

## Fitness function
- This function determine each individuals's fitness in a population
- The fitness score based on:
  - Individuals's performance
  - Ability to complete with others

## Genetic operator
- This operation change the genetic composition of the offsrpings -> ensure the offsprings is better than the parents

# Purpose of genetic algorithm

- Genetic algorithm is an iterative process to find the the best solution from a set of possible solution

## 3 general steps of Genetic algorithm
1. Initialize a random population P
2. Assess the fitness of the population
3. Perform the following iterative process until convergence is achieved

> [!IMPORTANT] 
> What is convergence ?
> - Convergence means either:
>   - Finding the desired or optimal results
>   - Reaching the maximum number of iterations

# Pseudocode

``` text
START
    Generate initial population
    Calculate the fitness
    REPEAT
        Calculate fitness
        Perform Selection + crossover at the same time
        Perform Mutation
    UNTIL population converges
STOP
```

# How does genetic algorithm work ?

> [!IMPORTANT] 
> 6 steps of Genetic algorithm
>    1. Setting up initial population
>    2. Determining fitness
>    3. Selection
>    4. Crossover
>    5. Mutation
>    6. Termination

## Setting up initial population
- As mentioned earlier, Population is made from chromosomes and chromosome is made from genes
- Gene can represent many type of value:
    - Binary value (0, 1)
    - Real value (float numbers)
    - Integer
    - Permutation representation

## Fitness function
- A fitness function return the fitness score of each chromosome
- The scores are then used to determine the probability of being selected for reproduction

## Selection
- This is the phase where the chromosome with high fitness score get choosen using selection operator
- There are many selection operators out there

### Roulette Wheel Selection
![Routelette Wheel Selection](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*C41PMDo7mVE9Kk5l.jpg)

- A roulette wheel with each n porpotion relative to n chromosome
- The fittness score will determine the portion of the chromosome in the roulette wheel
-> Higher score = bigger portion
- The wheel will then be spinned to choose the parents

