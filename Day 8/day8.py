with open('input.txt') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

example = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''.split('\n')

# input = example

import string
import numpy as np
from itertools import permutations

grid = np.array([[x for x in y] for y in input])

def get_coordinates(character, grid = grid):
    cols, rows = np.where(grid == character)
    coordinates = [x for x in zip(cols,rows)]
    return(coordinates)

def distance(c1, c2):
    return(tuple(map(lambda i,j: i-j, c1, c2)))

def translate(c, t):
    return(tuple(map(lambda i,j: i+j, c, t)))

def check_bounds(c, y, x):
    if 0 <= c[0] < y and 0 <= c[1] < x: return(1)
    return(0)

antinodes = []
for c in string.ascii_letters + string.digits:
    antennas = get_coordinates(c, grid)
    antinodes += [translate(x[0], distance(x[0], x[1])) for x in permutations(antennas, 2) if check_bounds(translate(x[0], distance(x[0], x[1])), grid.shape[0], grid.shape[1])]
    
part_1 = len(set(antinodes))

antinodes2 = []
for c in string.ascii_letters + string.digits:
    antennas = get_coordinates(c, grid)
    antinodes2 += antennas
    for x in permutations(antennas, 2):
        antinode_coord = translate(x[0], distance(x[0], x[1]))
        while check_bounds(antinode_coord, grid.shape[0], grid.shape[1]):
            antinodes2.append(antinode_coord)
            antinode_coord = translate(antinode_coord, distance(x[0], x[1]))

part_2 = len(set(antinodes2))