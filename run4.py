from queue import PriorityQueue
n = 10
k = 8
array = [[2, 4], [3, 9], [4, 5], [2, 8], [2, 4],
         [2, 10], [1, 4], [3, 7], [1, 3], [4, 6]]

queue = PriorityQueue()
for i in range(0, len(array)):
    priority_calculate = -(((array[i][0]+1)/(array[i][1]+1))-((array[i][0])/(array[i][1])))
    # print(priority_calculate)
    queue.put((priority_calculate, i, array[i]))


for i in range(0, k):
    priority, index, bag = queue.get()
    bag[0] += 1
    bag[1] += 1
    priority = -(((bag[0]+1)/(bag[1]+1))-((bag[0])/(bag[1])))
    queue.put((priority, index, bag))
    print(index, end=" ")


# while not queue.empty():
#     print(queue.get()[2], end=" ")