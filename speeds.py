import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
data = []
speed = int(input())
speed_limit = (speed * 1000) / 3600

light_count = int(input())
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    data.append([distance, duration])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
#speed_up = int(speed_meter) +1



def green_light(dist, duration):
    ''' Function that return YES if the light is green else return NO '''
    while dist > 0:
        print("dist   dur ",distance, duration,  file=sys.stderr, flush=True)
        green = int(distance / duration) % 2
        if dist > speed_up :
            dist -= distance / speed_up
        else:
            dist = 0
        print("dist   dur ", green, dist,  file=sys.stderr, flush=True)
    # Test if the light is GREEN when the car arrives DIST = 0
    if green == 0 and dist ==0:
        result = "yes"
    else:
        result = "no"

    return result

def better_speed(dist, duration):
    speed_min = dist / duration
    print("speed_min...",speed_min, file=sys.stderr, flush=True)
    if speed_min < speed_limit:
        result = speed
        return result

    for i in range(1,100):
        speed_max = dist / (duration * i )
        print("speed_max i...",speed_max, i , file=sys.stderr, flush=True)
        if speed_max < speed_limit:
            result = int(speed_max * 3600 / 1000)
            return result

def is_green(dist, duration, actual_speed):
    distance_at_speed = (actual_speed / 3.6) * duration
    if distance_at_speed > dist:
        print("actual_speed...dist",actual_speed ,distance_at_speed, file=sys.stderr, flush=True)
        result = actual_speed
    else:
        new_speed = (dist / duration) * 3.6
        while new_speed > speed:
            new_speed /= 2
        result = int(new_speed)
        print("new_speed.2..",new_speed , file=sys.stderr, flush=True)
    return result
    
# For each light check if its GREEN
speeds = []
actual_speed = speed
for dist, duration in data:
    print("dist dura...",dist, duration,  file=sys.stderr, flush=True)
    actual_speed = is_green(dist, duration, actual_speed)
    speeds.append(actual_speed)

print("speeds..",speeds,  file=sys.stderr, flush=True)
better = min(speeds)

'''
speeds = []
for dist, duration in data:
    print("dist dura...",dist, duration,  file=sys.stderr, flush=True)
    answer = better_speed(dist, duration)
    speeds.append(answer)

better = min(speeds)

print("better...",speeds, better,  file=sys.stderr, flush=True)

for dist, dura in data:
    result = green_light(dist, dura)
    print("result ",result, file=sys.stderr, flush=True)
'''

#green = int(distance / speed_up) % 2
print("speed, light...",speed, speed_limit, light_count, file=sys.stderr, flush=True)
print("data...", data, file=sys.stderr, flush=True)
#print("green...",green, file=sys.stderr, flush=True)
'''
answer = 0
if result == "yes":
    answer = speed

print(answer)
'''
print(better)
#print(actual_speed)
