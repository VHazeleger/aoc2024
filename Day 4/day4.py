with open('input.txt') as f:
    input = [x.replace('\n', '') for x in f.readlines()]

example = [[y for y in x] for x in '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''.split('\n')]

# input = example

# part 1
from collections import defaultdict

def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

def check_xmas(text):
    return(text.count('XMAS'))

cols = [''.join(x) for x in groups(input, lambda x, y: x)]
r_cols = [''.join(x[::-1]) for x in groups(input, lambda x, y: x)]
rows = [''.join(x) for x in groups(input, lambda x, y: y)]
r_rows = [''.join(x[::-1]) for x in groups(input, lambda x, y: y)]
fdiag = [''.join(x) for x in groups(input, lambda x, y: x + y)]
r_fdiag = [''.join(x[::-1]) for x in groups(input, lambda x, y: x + y)]
bdiag = [''.join(x) for x in groups(input, lambda x, y: x - y)]
r_bdiag = [''.join(x[::-1]) for x in groups(input, lambda x, y: x - y)]

full = cols + r_cols + rows + r_rows + fdiag + r_fdiag + bdiag + r_bdiag

result = sum(list(map(check_xmas, full)))

# part 2
import numpy as np
matrix = np.array([[y for y in x] for x in input])
rows, cols = np.where(matrix == 'A')
matrix = matrix.tolist()
coords = list(zip(rows.tolist(), cols.tolist()))

def check_x_mas(matrix, coord):
    ul = (-1,-1)
    ur = (-1,1)
    dl = (1,-1)
    dr = (1,1)
    
    top = 'MMSS'
    right = 'SMSM'
    bottom = 'SSMM'
    left = 'MSMS'
    
    pattern = ''.join([matrix[tuple(map(lambda i, j: i + j, coord, translation))[0]][tuple(map(lambda i, j: i + j, coord, translation))[1]] for translation in [ul, ur, dl, dr]])
    if pattern in [top, right, bottom, left]: return(1)
    return(0)

result = 0
for c in coords:
    print(c)
    if c[0] == 0 or c[0] == len(input)-1 or c[1] == 0 or  c[1] == len(input)-1: continue
    result += check_x_mas(matrix, c)

