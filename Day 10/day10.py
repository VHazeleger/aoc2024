with open('input.txt') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

example = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''.split('\n')

# input = example

input = [[int(y) for y in x] for x in input]

# part 1
import numpy as np
input_np = np.array(input)
cols, rows = np.where(input_np == 0)
trailheads = list(zip(cols.tolist(), rows.tolist()))

def next_steps(input, coord):
    val = input[coord[0]][coord[1]]
    N = (coord[0]-1, coord[1])
    E = (coord[0], coord[1]+1)
    S = (coord[0]+1, coord[1])
    W = (coord[0], coord[1]-1)
    # print(N, E, S, W)

    steps = []
    for option in [N,E,S,W]:
        if option[0] < 0 or option[0] > len(input)-1 or option[1] < 0 or option[1] > len(input[0])-1: continue
        if input[option[0]][option[1]] != val+1: continue
        steps.append(option)
    
    return(steps)

def dfs(input, coord):
    total = 0
    check = [coord]
    reachable = []
    while len(check) > 0:
        next = check.pop(0)
        if input[next[0]][next[1]] == 9:
            reachable.append(next)
            total += 1
        else:
            check += next_steps(input, next)

    return({'reachable': reachable, 'total': total})

result1 = sum([len(set(x['reachable'])) for x in [dfs(input, t) for t in trailheads]])
result2 = sum([dfs(input, t)['total'] for t in trailheads])