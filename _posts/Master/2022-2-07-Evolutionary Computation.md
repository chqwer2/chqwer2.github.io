---
layout:     post
title:      "Evolutionary Computation Week 1"
subtitle:   " \"Get familiar with the Evolutionary Computation.\""
date:       2022-02-01 12:00:00
author:     "Calvchen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:

   - Python
   - Pandas
   - Data
   - ML
   - Evo Comp

subtitle:   " \"Get familiar with the EC...\""




---

> “The study of computational systems that use ideas inspired from natural evolution, e.g., the principle of survival of the fittest.”

# Evolutionary Computation

EC provides a general method for solving ‘search for solutions’ type of problems, such as optimisation, learning, and design.

## Progress:

Week 2…



## What will be covered?

**Algorithms** 

- Randomized Search Heuristics 
- Evolutionary Algorithms: [Genetic Algorithms](#Genetic Algorithm (GA)), Genetic Programming, Evolutionary Programming, Differential Evolution and Evolution Strategies 
- Game Theory (optimisation) and Evolutionary Game Theory (dynamics) 
- Particle Swarm Optimiser & Ant Colony Optimisation 
- Artificial Immune System

**Theory** 

- Schema Theorem -
- Convergence and Convergence Rate -
- Computational Complexity -
- No Free Lunch Theorem 
- Fitness Landscape 
- Boolean Networks 
- Cellular Automata (including Game of Life)

### Categories of Algorithms by by design paradigm

- Divide and conquer algorithms, e.g., quicksort algorithm 
- Dynamic programming algorithms 
- Mathematical programming algorithms, e.g., linear programming 
- Search and enumeration algorithms 
  - Brute force (exhaustive) algorithms, enumerating all possible candidate solutions and check 
  - Improved brute force algorithms, e.g., branch and bound algorithms 
  - **Heuristic algorithms** 
    - Local search, e.g., greedy search 
    - **Randomised algorithms**, which include Evolutionary Computation, etc



#### Start with Questions

**Matching one Bolt to n Distinct Sizes Nuts:**

given one bolt and a collection of n nuts of different sizes, find a nut match the bolt

The brute-force solution time complexity: O(n2)

**Answer:** For many problems, a randomised algorithm is the simplest, the fastest.



**Heuristic Algo**

CS definition of **heuristic**:  a (usually simple) algorithm that produces a good enough solution for a problem in a reasonable time frame

heuristic: find or discover non-optimal but satisfactory

Trad of optimality, completness, accuracy or precision for **speed**.

Includes determiistic (e.g. 0 or 1 results)

### Randomised Algo

makes random choices during execution,

output and runtime can vary even with fixed input.



Use random number to help find and improve the solutions.

##### Two representatives:

- Las Vegas Algo

  may result in infinite loop until the correct solution

  ```
  Repeat:
  	Random search 1 element out of n samples.
  	until a == x
  end
  ```

  the worst runtime complexity is unbound

- Monte Carlo Algo (蒙特卡罗)

  runs for a fixed number of steps

  ```
  i = 0
  Repeat:
  	Random search 1 element out of n samples.
  	i += 1;
  	until (a == x) || (i == k)
  end
  ```

​		O(1) is fixed



##### Randomised Quicksort Algo

avg: O(nlogn), worst: O(2nlogn)

![image-20220203123055102](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220203123055102.png)



### Genetic Algorithm (GA)

– natrual selection: survival of the fittest

**Observation:** Natural Evolution has evolved many complex systems (e.g., brain) and ”solved” many bioengineering problem. 

**Idea:** GA mimics the idea of Darwinian Evolution to optimize some objective.

**Keywords:** Genotype (基因型), Phenotype (表现型), Chromosomes (染色体)

The Initialization requires many setting, including initial population, population size, selection, reproduction, mutation, and criteria for termination of algorithm



**Change** or genetic variation comes from: 

- **Mutations**: changes in the DNA (Deoxyribonucleic Acid) sequence, 
- **Crossover**: reshuffling of genes through sexual reproduction and migration between populations



**Driving Force:** Simulate Genetic variations that enhance survival and reproduction become and remain more common in successive generations of a population.



music … 

