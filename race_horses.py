import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
data = []
n = int(input())
for i in range(n):
    pi = int(input())
    data.append(pi)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# My code
# order the list data to compare easily the numbers
data.sort()
difference = max(data)  # set the higher value for difference
# Comare two following numbers
for nb in range(n-1):
    if data[nb + 1] - data[nb] < difference:
        difference = data[nb +1] - data[nb]

print("diff finale...",difference, file=sys.stderr, flush=True) 
print(difference)
