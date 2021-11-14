import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

words = []
points = {"a": 1, "e": 1, "i": 1, "o": 1, "n": 1, "r": 1,
"t": 1, "l": 1, "s": 1, "u": 1,
"d": 2, "g": 2,
"b": 3, "c": 3, "m": 3, "p": 3,
"f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
"k": 5,
"j": 8, "x": 8,
"q": 10, "z": 10
}


n = int(input())
for i in range(n):
    w = input()
    # 0 - Remove all words larger than 7 letters
    if len(w) > 7:
        next
    else:
        words.append(w)

letters = sorted(input())
print(" Number of words..", len(words), file=sys.stderr, flush=True)
print(" my letters...", letters, file=sys.stderr, flush=True)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# MY CODE ////

# 1 - Fill the list list 'bad' with words not possible
bad = []
for w in words:
    used = letters.copy()
    for le in w:
        if le in used:
            used.remove(le)
        else:
            if w not in bad:
                bad.append(w)

# 2 - Remove bad words in the list
for word in bad:
    words.remove(word)

# 3 - Calculate the points of the words possible
word_point = {}
for w in words:
    word_point[w] = 0
    for l in w:
        word_point[w] += points[l]


# 5 - Choose the word with the greatest number of points
result = max(word_point, key=word_point.get)
print("max word...", result, file=sys.stderr, flush=True)

# 6 - Print the result
print(result)
