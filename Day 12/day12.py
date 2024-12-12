with open('input.txt') as f:
    input = f.read().strip()

import numpy as np

input = np.array([[x for x in y] for y in input.split('\n')])
examples = [np.array([[z for z in y] for y in x.split('\n')]) for x in [
    'AAAA\nBBCD\nBBCC\nEEEC'.strip(),
    'OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO'.strip(),
    'RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE'.strip(),
    'EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE'.strip(),
    'AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA'.strip()]
]

# input = examples[0]

def neighbours(coord):
    N = (coord[0]-1, coord[1])
    S = (coord[0]+1, coord[1])
    E = (coord[0], coord[1]+1)
    W = (coord[0], coord[1]-1)
    return([N,E,S,W])

def check_oob(coord, n_rows, n_cols):
    if coord[0] < 0 or coord[1] < 0 or coord[0] >= n_rows or coord[1] >= n_cols:return(True)
    return(False)

def check_letter(value, letter):
    if value == letter: return(True)
    return(False)

def check_invalid(input, coord, letter):
    if check_oob(coord, input.shape[0], input.shape[1]) or not check_letter(input[coord[0]][coord[1]], letter): return(True)
    return(False)

def part_1(input):
    identified = []
    result = []
    n_rows, n_cols = input.shape
    for y in range(n_rows):
        for x in range(n_cols):
            if (y,x) in identified: continue
            letter = input[y][x]
            n_perimiters = 0
            n_plots = 0
            check_list = [(y,x)]
            while len(check_list) > 0:
                c = check_list.pop(0)
                n_plots += 1
                for n in neighbours(c):
                    # out of bounds:
                    if check_oob(n, n_rows, n_cols): 
                        n_perimiters += 1
                        continue
                    # already identified:
                    if n in identified:
                        flag = 0 if check_letter(input[n[0]][n[1]], letter) else 1
                        n_perimiters += flag 
                        continue
                    # different letter:
                    elif not check_letter(input[n[0]][n[1]], letter):
                        n_perimiters += 1
                        continue
                    # implicit else:
                    if n not in check_list: check_list.append(n)
                identified.append(c)
            result.append((letter, n_perimiters, n_plots))

    return(sum([x[1]*x[2] for x in result]))

def diag_neighbours(coord):
    NE = (coord[0]-1, coord[1]-1)
    SW = (coord[0]+1, coord[1]+1)
    NW = (coord[0]-1, coord[1]+1)
    SE = (coord[0]+1, coord[1]-1)
    return([NE,NW,SE,SW])

def compute_corners(input, coord, correct_letter):
    nesw_neighbours = neighbours(coord)
    diagon_neighbours = diag_neighbours(coord)

    nesw_invalid = [check_invalid(input, x, correct_letter) for x in nesw_neighbours]
    diag_invalid = [check_invalid(input, x, correct_letter) for x in diagon_neighbours]

    corners = 0

    corners += sum(
        [
            (nesw_invalid[0] and nesw_invalid[3]),
            (nesw_invalid[3] and nesw_invalid[2]),
            (nesw_invalid[1] and nesw_invalid[2]),
            (nesw_invalid[0] and nesw_invalid[1]),
            ((not nesw_invalid[0] and not nesw_invalid[3]) and diag_invalid[0]),
            ((not nesw_invalid[3] and not nesw_invalid[2]) and diag_invalid[2]),
            ((not nesw_invalid[1] and not nesw_invalid[2]) and diag_invalid[3]),
            ((not nesw_invalid[0] and not nesw_invalid[1]) and diag_invalid[1])
        ]
        )
    
    return(corners)

def part_2(input):
    identified = []
    result = []
    n_rows, n_cols = input.shape
    for y in range(n_rows):
        for x in range(n_cols):
            if (y,x) in identified: continue
            letter = input[y][x]
            n_sides = 0
            n_plots = 0
            check_list = [(y,x)]
            while len(check_list) > 0:
                c = check_list.pop(0)
                n_plots += 1
                n_sides += compute_corners(input, c, letter)

                for n in neighbours(c):
                    # out of bounds:
                    if n[0] < 0 or n[1] < 0 or n[0] >= input.shape[0] or n[1] >= input.shape[1]:
                        continue
                    # already identified:
                    if n in identified:
                        continue
                    # different letter:
                    elif input[n[0]][n[1]] != letter:
                        # n_perimiters += 1
                        continue
                    # implicit else:
                    if n not in check_list: check_list.append(n)
                identified.append(c)
            result.append((letter, n_plots, n_sides))

    return(sum([x[1]*x[2] for x in result]))