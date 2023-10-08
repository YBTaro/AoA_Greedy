from queue import PriorityQueue
import random
import numpy as np
import matplotlib.pyplot as plt

from run1 import strat1
from run2 import strat2
from run3 import strat3
from run4 import strat4

def experiment(n_array, array, k_array): # give the number of total devices and working devices, return the result of using four greedy algos
    experiment_result = {k: [[] for _ in range(4)] for k in k_array} # dictionary {k1:[[],[],[],[]], k2:[[],[],[],[]],k3:[[],[],[],[]],}
    # 做一個k_array_change，紀錄 k(i)-k(i-1)的值
    k_array_change = {k_array[0]: k_array[0]}
    for i in range(1, len(k_array)):
        k_array_change[k_array[i]] = k_array[i]- k_array[i-1]

    # print(k_array)
    # print(k_array_change)
    # -------------------------
    # array 是字典，key 是 n， value 是 array(這個array的長度為n，每個 element 的結構 (work, total))
    for n in n_array:
        # copy 初始的array，做四個不同地址，但值相同的array給演算法使用。這四個array每次用strat分派devices後，值會跟著變
        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        arrN = [arr1, arr2, arr3, arr4]
        for i in range(4):
            for element_array in array[n]:
                arrN[i].append(element_array.copy())

        for k, result in experiment_result.items():
            # 因為傳址，所以用k_array_change[k]當參數。假設 n = 1000, k = 800,900，當算k=900時，傳入演算法的k是100，因為會用k=800的結果繼續往後做
            results = [strat1(n, k_array_change[k], arr1, False),
                        strat2(n, k_array_change[k], arr2, False),
                        strat3(n, k_array_change[k], arr3, False),
                        strat4(n, k_array_change[k], arr4, False)]
            for i, arr in enumerate(result):
                arr.append(results[i])

        
    # for k, result in experiment_result.items():


    #     for n in n_array: # do len(n_array) times
    #         # copy array
    #         arr1 = []
    #         arr2 = []
    #         arr3 = []
    #         arr4 = []
    #         arrN = [arr1, arr2, arr3, arr4]
    #         for i in range(4):
    #             for element_array in array[n]:
    #                 arrN[i].append(element_array.copy())

    #         results = [ # problem : does all the strat use the same array?
    #             strat1(n, k, arr1, False), # ****array is a dictionary**** array[n] is the randomly created array with exactly n bags
    #             strat2(n, k, arr2, False),
    #             strat3(n, k, arr3, False),
    #             strat4(n, k, arr4, False)
    #         ]
    #         for i, arr in enumerate(result): # result = [[],[],[],[]] arr = [n等於1000,2000, 3000時，計算的結果]
    #             arr.append(results[i])
    print(experiment_result)
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
    n_array = [100, 200, 300]
    k_array = [1000, 2000, 3000, 4000, 5000]

    array = {n: [] for n in n_array} # dictionary {n1:[],n2:[],n3:[]} This is a dictionary named "array" lol
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
