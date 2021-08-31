import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
print("n l e...",n,l,e, file=sys.stderr, flush=True)
graph = dict()
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    # /// MY CODE ///
    # Create the graph
    # print("n1 n2...",n1, n2, file=sys.stderr, flush=True)
    if n1 not in graph.keys():
        graph[n1] = []
    if n2 not in graph[n1]:
        graph[n1] += [n2]
    if n2 not in graph.keys():
        graph[n2] = []
    if n1 not in graph[n2]:
        graph[n2] += [n1]
    # print("graph...",graph, file=sys.stderr, flush=True)

exits = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    # Create the list of exits
    exits.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    # /// MY CODE ///
    # Boucle to check every exit 'ei'
    for node in exits:
        # Check a direct link between 'si' and 'ei'
        if node in graph[si]:
            result = str(si) + " " + str(node)
            # print("result...",result, file=sys.stderr, flush=True)
            break
        else:
            result = str(si) + " " + str(graph[si][0])

    print(result)


        
        

            

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    #print("0 1")
