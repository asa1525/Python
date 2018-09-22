import math
queue = [4, 7, 1, 9, 12, 0, 5, 2]
queue[3] = queue[3] + queue[0]
while queue[6] < queue[1]:
    queue[1] = queue[1] + 7
    queue[3] = queue[3] - queue[7]
    queue[6] = queue[1] - queue[3]
print(queue[6])
