from queue import PriorityQueue

# calculate priority value
def priority_calculate(numWork, total):
    return (numWork+1)/(total+1)-numWork/total

def strat4(n, k, array, print_result=True):
    # print(array)
    queue = PriorityQueue()
    for i, arr in enumerate(array):
        # want the max, so add negative sign to priority value
        queue.put((-priority_calculate(arr[0], arr[1]), i, arr))

    result = ""
    for i in range(0, k):   # put k devices one by one
        _, index, bag = queue.get() # selected one is out of queue
        bag[0] += 1 # numWorking
        bag[1] += 1 # total
        queue.put((-priority_calculate(bag[0], bag[1]), index, bag)) # change values and put it back to queue
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

    strat4(n, k, array)