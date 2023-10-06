from queue import PriorityQueue
import random
import numpy as np
import matplotlib.pyplot as plt

from run1 import strat1
from run2 import strat2
from run3 import strat3
from run4 import strat4


def run1(n, k, array): # return average percentage with n = total devices , k = num of work devices
    queue = PriorityQueue()
    for i, arr in enumerate(array):
        queue.put((arr[0], i, arr))

    for i in range(0, k):
        priority, index, bag = queue.get()
        bag[0] += 1
        bag[1] += 1
        queue.put((bag[0], index, bag))

    percentage = 0
    for bag in array:
        percentage += (bag[0]/bag[1])

    percentage = (percentage/n)*100
    return round(percentage, 2)


def run2(n, k, array):
    queue = PriorityQueue()
    for i, arr in enumerate(array):
        queue.put((arr[0]/arr[1], i, arr))

    for i in range(0, k):
        priority, index, bag = queue.get()
        bag[0] += 1
        bag[1] += 1
        queue.put((bag[0]/bag[1], index, bag))

    percentage = 0
    for bag in array:
        percentage += (bag[0]/bag[1])

    percentage = (percentage/n)*100
    return round(percentage, 2)


def run3(n, k, array):
    queue = PriorityQueue()
    for i, arr in enumerate(array):
        queue.put((arr[1], i, arr))

    for i in range(0, k):
        priority, index, bag = queue.get()
        bag[0] += 1
        bag[1] += 1
        queue.put((bag[1], index, bag))

    percentage = 0
    for bag in array:
        percentage += (bag[0]/bag[1])

    percentage = (percentage/n)*100
    return round(percentage, 2)


def priority_calculate(numWork, total):
    return (numWork+1)/(total+1)-numWork/total


def run4(n, k, array):
    queue = PriorityQueue()
    for i, arr in enumerate(array):
        queue.put((-priority_calculate(arr[0], arr[1]), i, arr))

    for i in range(0, k):
        priority, index, bag = queue.get()
        bag[0] += 1
        bag[1] += 1
        queue.put((-priority_calculate(bag[0], bag[1]), index, bag))

    percentage = 0
    for bag in array:
        percentage += (bag[0]/bag[1])

    percentage = (percentage/n)*100
    return round(percentage, 2)


def experiment(n, k): # give the number of total devices and working devices, return the result of using four greedy algos
    array1 = []
    for i in range(n): # randomly create array with n total devices
        total = random.randint(0, 9999)
        n_work = random.randint(0, total)
        array1.append([n_work, total])
    array2 = array1.copy() # since every greedy algo would change the value in the array, use array.copy to create different array with the same original values
    array3 = array1.copy()
    array4 = array1.copy()
    return [run1(n, k, array1), run2(n, k, array2), run3(n, k, array3), run4(n, k, array4)]
    # return [strat1(n, k, array1, False), strat2(n, k, array2, False), strat3(n, k, array3, False), strat4(n, k, array4, False)]

def plot_result(n_array, result, k):
    fig, ax = plt.subplots(2, 2)
    fig.suptitle("k = %d"%k)
    cur_strat = 1
    for i in range(2):
        for j in range(2):
            ax[i, j].plot(n_array, result[cur_strat-1])
            ax[i, j].set_title("Strategy%d"%cur_strat)
            ax[i, j].set_xlabel("n")
            ax[i, j].set_ylabel("Percentage")
            cur_strat += 1
    plt.tight_layout()
    plt.show()

def main():
    experiment_result = []
    n_array, k = [1000, 2000, 3000, 4000, 5000], 800
    experiment_result = [[] for _ in range(4)]
    for n in n_array:
        result = experiment(n, k)
        # experiment_result.append(experiment(n, k))
        for i, arr in enumerate(experiment_result):
            arr.append(result[i])
    print(experiment_result) # experiment_result[i] would return an array of four elements, which are [run1, run2, run3, run4]'s result respectively. The length of experiment_result would be the length of n_array
    plot_result(n_array, experiment_result, k)

if __name__ == "__main__":
    main()
