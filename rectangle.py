import sys
import math


w, h, c_x, c_y = [int(i) for i in input().split()]
#print("w..h",w,h,c_x, c_y, file=sys.stderr, flush=True)

hor = [0, w]
ver = [0, h]
for i in input().split():
    hor.append(int(i))
for i in input().split():
    ver.append(int(i))

# Order the list of points
hor = sorted(hor)
ver = sorted(ver)


# Test each angles
count = 0
for basex in hor:
    for basey in ver:
        for x in hor[hor.index(basex)+1:]:
            for y in ver[ver.index(basey)+1:]:
                if basex - x == basey - y:
                    # if a square samme value in each side
                    count += 1
                    




print(count)
