from queue import PriorityQueue

n, k = input().split()
n, k = int(n), int(k)
array = []
for i in range(n):
    numWork, total = input().split()
    array.append([int(numWork), int(total)])

def priority_calculate(numWork, total):
    return -(((numWork+1)/(total+1))-(numWork/total))

queue = PriorityQueue()
for i, arr in enumerate(array):
    queue.put((priority_calculate(arr[0], arr[1]), i, arr))


for i in range(0, k):
    priority, index, bag = queue.get()
    bag[0] += 1
    bag[1] += 1
    priority = -(((bag[0]+1)/(bag[1]+1))-((bag[0])/(bag[1])))
    queue.put((priority, index, bag))
    print(index, end=" ")


# while not queue.empty():
#     print(queue.get()[2], end=" ")