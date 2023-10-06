from queue import PriorityQueue

def strat3(n, k, array, print_result=True):
    queue = PriorityQueue()
    for i, arr in enumerate(array):
        queue.put((arr[1], i, arr))


    for i in range(0, k):
        _, index, bag = queue.get()
        bag[0] += 1
        bag[1] += 1
        queue.put((bag[1], index, bag))
        if print_result:
            print(index, end=" ")

    percentage = 0
    while (not queue.empty()):
        _, _, bag = queue.get()
        percentage += bag[0]/bag[1]
    
    return round(100*percentage/n, 2)

if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    array = []
    for i in range(n):
        numWork, total = input().split()
        array.append([int(numWork), int(total)])

    strat3(n, k, array)