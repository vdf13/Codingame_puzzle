import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
print("initial...",nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators, file=sys.stderr, flush=True)
elevators_dic = {}

for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    
    elevators_dic[elevator_floor] = elevator_pos

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)



    # /// MY CODE ///
    # if clone not in the map return WAIT
    if clone_floor == -1:
        result = "WAIT"
    else:
        # Define the target for the clones
        if exit_floor == clone_floor:
            target = exit_pos
        else:
            target = elevators_dic[clone_floor]
        print("clones...",clone_floor, clone_pos, direction, "target.", target, file=sys.stderr, flush=True)

        # Define the corect direction per floor
        if clone_pos > target and direction == "RIGHT":
            result = "BLOCK"
        elif clone_pos < target and direction == "LEFT":
            result = "BLOCK"
        else:
            result = "WAIT"
    
    # action: WAIT or BLOCK
    print(result)
