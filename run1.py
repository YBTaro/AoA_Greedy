from queue import PriorityQueue

n, k = input().split()
n, k = int(n), int(k)
array = []
for i in range(n):
    numWork, total = input().split()
    array.append([int(numWork), int(total)])

queue = PriorityQueue()
for i, arr in enumerate(array):
    queue.put((arr[0], i, arr))

for i in range(0, k):
    priority, index, bag = queue.get()
    bag[0] += 1
    bag[1] += 1
    queue.put((bag[0], index, bag))
    print(index, end=" ")


# while not queue.empty():
#     print(queue.get()[2], end=" ")
