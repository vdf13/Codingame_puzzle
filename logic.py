import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())

# Functions
def convert_digit(texte):
    result = []
    # return a list of 0 or 1 consant the input _-
    for sig in texte:
        if sig == "_":
            result.append(0)
        else:
            result.append(1)
    return result

def convert_signal(texte):
    # return a string with -_ consant the input 0 or 1
    result = ""
    for digit in texte:
        if digit == 0:
            result += "_"
        else:
            result += "-"
    return result

def boolean(operation):
    # return a list of 0 - 1 after the boolean operation
    result = []
    ope, first, second = operation
    first = input_data[first]
    second = input_data[second]
    for i in range(len(first)):
        if ope == "AND":
            rr = first[i] & second[i]
        elif ope == "OR":
            rr = first[i] | second[i]
        elif ope == "XOR":
            rr = first[i] ^ second[i]
        elif ope == "NAND":
            rr = not(first[i] & second[i])
        elif ope == "NOR":
            rr = not(first[i] | second[i])
        elif ope == "NXOR":
            rr = not(first[i] ^ second[i])

        result.insert(i, rr)
    return result

input_data = {}
for i in range(n):
    input_name, input_signal = input().split()
    input_data[input_name] = convert_digit(input_signal)

output_data = {}
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    output_data[output_name] = [_type, input_name_1, input_name_2]

for key in output_data.keys():
    response = [] 
    # make the logical operation
    response = boolean(output_data[key])
    # Convert to a signal
    response = convert_signal(response)
    # format the response
    response = key + " " + response

    print(response)
