with open('input.txt') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

example = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''.split('\n')

# input = example

import numpy as np

map = np.array([[y for y in x] for x in input])

def walk_maze(map = map):
    
    rows, cols = map.shape
    y,x = (int(x) for x in np.where(map == '^'))
    copy_map = np.copy(map) # to check

    guard_positions = 0
    direction = 'up'
    steps = {}
    passed_steps = []

    while x >= 0 and y >= 0 and x < rows and y < cols:
        # print(x,y)
        current_step = f'{y},{x},{direction}'
        # print(current_step)
        if current_step in passed_steps: 
            # print("Infinite...")
            # print(copy_map)

            # print('\n'.join([''.join(x) for x in copy_map]))
            return({
                'guard_positions': guard_positions,
                'steps': steps,
                'walked_map': copy_map,
                'infinite': 1
            })
        passed_steps.append(current_step)
        if copy_map[y][x] != 'X': 
            guard_positions += 1
            copy_map[y][x] = 'X'
            if (y,x) != tuple(int(x) for x in np.where(map == '^')):
                steps[f'{y},{x}'] = steps.get(f'{y},{x}', 0) + 1

        # print(copy_map)

        if direction == 'up':
            if y-1 < 0: break
            if map[y-1][x] == '#': direction = 'right'; continue
            y -= 1
        elif direction == 'right':
            if x+1 >= cols: break
            if map[y][x+1] == '#': direction = 'down'; continue
            x += 1
        elif direction == 'down':
            if y+1 >= rows: break
            if map[y+1][x] == '#': direction = 'left'; continue
            y += 1
        elif direction == 'left':
            if x-1 < 0: break
            if map[y][x-1] == '#': direction = 'up'; continue
            x -= 1

    return({
        'guard_positions': guard_positions,
        'steps': steps,
        'walked_map': copy_map,
        'infinite': 0
    })
    

# part 2
steps = walk_maze()['steps']
infinites = 0
for s in steps.keys():
    y,x = [int(x) for x in s.split(',')]
    print(list(steps.keys()).index(s), len(steps.keys()))
    test_map = map.copy()
    test_map[y][x] = '#'
    infinites += walk_maze(map = test_map)['infinite']