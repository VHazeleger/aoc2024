with open('input.txt') as f:
    input = f.read().strip()

robots = [[tuple([int(z) for z in y.replace('p=','').replace('v=','').split(',')]) for y in x.split(' ')] for x in input.split('\n')]    

positions = [r[0] for r in robots]
velocities = [r[1] for r in robots]

def update_position(p,v):
    new_position = list(map(sum,zip(p,v)))
    if new_position[0] < 0:
        new_position[0] += 101
    if new_position[1] < 0:
        new_position[1] += 103
    if new_position[0] > 100:
        new_position[0] %= 101
    if new_position[1] > 102:
        new_position[1] %= 103
    return(tuple(new_position))

import time
def print_map(positions):
    map = [['.' for i in range(101)] for j in range(103)]
    for p in positions:
        map[p[1]][p[0]] = '#'
    result = [''.join(r) for r in map]
    if any(['#####' in r for r in result]):
        print('\n'.join([r for r in result]))
        time.sleep(1)

new_positions = positions
for i in range(9999):
    print(i+1)
    new_positions = list(map(update_position, new_positions, velocities))
    print_map(new_positions)

q1 = len([x for x in new_positions if x[0] < 50 and x[1] < 51])
q2 = len([x for x in new_positions if x[0] > 50 and x[1] < 51])
q3 = len([x for x in new_positions if x[0] < 50 and x[1] > 51])
q4 = len([x for x in new_positions if x[0] > 50 and x[1] > 51])

result = q1*q2*q3*q4

