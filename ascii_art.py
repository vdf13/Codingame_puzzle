import sys
import math
import string


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
lettres = list(string.ascii_uppercase) 
lettres.append("?")
ligne=[]

l = int(input())
h = int(input())
t = input().upper()


for i in range(h):
    row = input()
    ligne.append(row)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Fill the array with the number of l
result = []
for larg in range(l+1):
    result.append("")

# trouver l'index de la lettre

for haut in range(h):
    for let in t:
        if let not in lettres:
            let = "?"
        ind = lettres.index(let)
        result[haut] += (ligne[haut][l * ind:l * ind + l])
    print(result[haut])
