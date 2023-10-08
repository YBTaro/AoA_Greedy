from queue import PriorityQueue
import random
import numpy as np
import matplotlib.pyplot as plt

from run1 import strat1
from run2 import strat2
from run3 import strat3
from run4 import strat4

def experiment(n_array, array, k_array): # give the number of total devices and working devices, return the result of using four greedy algos
    experiment_result = {k: [[] for _ in range(4)] for k in k_array}
    for k, result in experiment_result.items():
        for n in n_array:
            results = [
                strat1(n, k, array[n], False),
                strat2(n, k, array[n], False),
                strat3(n, k, array[n], False),
                strat4(n, k, array[n], False)
            ]
            for i, arr in enumerate(result):
                arr.append(results[i])
    return experiment_result

def plot_result(n_array, result, k):
    fig_width = int(len(n_array)*3)
    fig, ax = plt.subplots(figsize=(fig_width,8))
    fig.suptitle("k = %d"%k, fontsize=20)
    width = 0.4
    x = np.arange(0, 2*len(n_array), 2)
    for cur_strat in range(4):
        rects = ax.bar(x-0.6+width*cur_strat, result[cur_strat], width)
        ax.bar_label(rects, padding=0.3)
    plt.xticks(x, n_array)
    plt.yticks(np.arange(0, 101, 10))
    ax.set_xlabel("n")
    ax.set_ylabel("Percentage (%)")
    plt.legend(["Strategy%d"%(i+1) for i in range(4)])
    plt.savefig("experiment_figs/k_%d"%k)
    # plt.show()

def main():
    n_array = [1000, 2000, 3000, 4000, 5000]
    k_array = [100, 500, 800, 1000]

    array = {n: [] for n in n_array}
    for n, arr in array.items():
        for _ in range(n): # randomly create array with n total devices
            total = random.randint(0, 9999)
            n_work = random.randint(0, total)
            arr.append([n_work, total])
    
    results = experiment(n_array, array, k_array)
    for k, result in results.items():
        plot_result(n_array, result, k)

if __name__ == "__main__":
    main()
