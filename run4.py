from queue import PriorityQueue

def priority_calculate(numWork, total):
    return (numWork+1)/(total+1)-numWork/total

def strat4(n, k, array, print_result=True):
    queue = PriorityQueue()
    for i, arr in enumerate(array):
        # want the max, so add negative sign to priority_calculate
        queue.put((-priority_calculate(arr[0], arr[1]), i, arr))

    for i in range(0, k):
        _, index, bag = queue.get()
        bag[0] += 1
        bag[1] += 1
        queue.put((-priority_calculate(bag[0], bag[1]), index, bag))
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

    strat4(n, k, array)