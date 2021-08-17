import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
# print("n, q...", n, q, file=sys.stderr, flush=True)

# Initialize the dict of MIME types
mime = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime[ext.lower()] = mt


for i in range(q):
    fname = input()  # One file name per line.
    # print("fname...", fname, file=sys.stderr, flush=True)

    # start of my code
    # Test if there is a dot in the file name
    if "." in fname:
        extension = fname.split(".")
        # Choose the last element and put it in lower case
        extension = extension.pop().lower()

        # test if the extension is in the mime dict
        if extension in mime.keys():
            result = mime[extension]
        else:
            result = "UNKNOWN"
    else: 
        # invalid extension return "UNKNOWN"
        result = "UNKNOWN"
    print(result)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
# print("answer")
