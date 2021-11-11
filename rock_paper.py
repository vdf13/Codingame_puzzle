import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# MY DATAS ///
players = {}
players_table = []
opp_table = {}
# dict of decision of winers Rock (R) Paper (P) sCissors (C) Lizard (L) Spock (S)
win_table = {"C": ["P", "L", ],
"L": ["S", "P", ],
"P": ["R", "S", ],
"R": ["C", "L", ],
"S": ["C", "R", ]
}

n = int(input())
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    players[numplayer] = signplayer
    players_table.append(numplayer)
    opp_table[numplayer] = ""

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Define the Function
def battle(op1, op2):
    ''' Function to find the winner between 2 opponents, 
    the winner is find with the table of decision win_table
    store the opponents of the player
    return the number of the winner
    '''
    if players[op1] in win_table[players[op2]]:
        opp_table[op2] += str(op1) + " "
        return op2
    elif players[op2] in win_table[players[op1]]:
        opp_table[op1] += str(op2) + " "
        return op1
    else:
        win = min(op1, op2)
        loose = max(op1, op2)
        opp_table[win] += str(loose) + " "
        return win

# MY CODE /// Begin of the game
print("players...", players ,file=sys.stderr, flush=True)
print("players_table..", players_table ,file=sys.stderr, flush=True)

while len(players_table) > 1:
    turn = len(players_table)
    for i in range(0,len(players_table),2):
        win = battle(players_table[i], players_table[i+1])
        players_table.append(win)
    del players_table[0:turn]

# Print the result
win = players_table.pop()
print(win)
print(opp_table[win].rstrip())
