import sys
import math

row = []
coords = []
stck = []
visited = []
l = int(input())
h = int(input())
for i in range(h):
    # saving map
    line = []
    for j in input():
        line.append(j)
    row.append(line)
n = int(input())
for i in range(n):
    # saving coordinates
    x, y = [int(j) for j in input().split()]
    coords.append([x, y])
for i in range(n):
    stck.append(coords.pop(0))
    sum = 0
    while stck:
        # iterating through the stack that contains cells
        x, y = stck.pop(0)
        if x >= 0 and x < l and y >= 0 and y < h and row[y][x] == 'O':
            # checking if call is water, if so adds 1 to sum and adds all neighbors to stack
            row[y][x] = 'V'
            visited.append([x, y])
            sum += 1
            stck.append([x+1, y])
            stck.append([x, y+1])
            stck.append([x-1, y])
            stck.append([x, y-1])
    print(sum)
    for x, y in visited:
        #changes the map to its original form
        row[y][x] = 'O'
