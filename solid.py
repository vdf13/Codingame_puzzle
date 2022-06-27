import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# My code
# Convert n to base 9
nine = 0
i = 0

while n != 0:
    rem = n % 9
    # Remove any 0 from the result
    if rem == 0:
        rem = 9
        n -=1

    nine = nine + rem * (10**i)
    n = n // 9
    i += 1

print(nine)
