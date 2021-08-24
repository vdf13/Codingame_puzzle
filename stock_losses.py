import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
data = []
n = int(input())
for i in input().split():
    v = int(i)
    data.append(v)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print("initial...",n,data, file=sys.stderr, flush=True)


# my code
higher = 0
loss = []

# Boucle to compare each value, store the higher value
# If a i is lower than higher value loss is stored in a list
for i in data:
    if i > higher:
        higher = i

    if i < higher:
        loss.append( i - higher )

# If there is no loss return 0 as a value
if len(loss) != 0:
    loss = min(loss)
else:
    loss = 0


print(loss)
