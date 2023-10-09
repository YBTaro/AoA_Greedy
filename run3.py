from queue import PriorityQueue

def strat3(n, k, array, print_result=True):
    queue = PriorityQueue()
    for i, arr in enumerate(array):
        queue.put((arr[1], i, arr)) # put element according to total

    result = ""
    for i in range(0, k):   # put k devices one by one
        _, index, bag = queue.get() # selected one is out of queue
        bag[0] += 1 # numWorking
        bag[1] += 1 # total
        queue.put((bag[1], index, bag)) # change values and put it back to queue
        result += "%d "%index
    
    if print_result:
        print(result)

    percentage = 0
    while (not queue.empty()):
        _, _, bag = queue.get()
        percentage += bag[0]/bag[1]
    
    return round(100*percentage/n, 2)   # return final percentage

if __name__ == "__main__":
    n, k = input().split()  # input reader
    n, k = int(n), int(k)   # type casting
    array = []
    for i in range(n):
        numWork, total = input().split()
        # 2d-array, 1st column is numWorking, 2nd is total
        array.append([int(numWork), int(total)])

    strat3(n, k, array)