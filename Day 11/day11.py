with open('input.txt') as f:
    input = f.read().strip()

example = '125 17'

# example = input

input = [int(x) for x in input.split(' ')]

from functools import cache

@cache
def apply_rules(stone):
    if stone == 0:
        return([1])
    elif len(str(stone)) % 2 == 0:
        return([int(str(stone)[0:int(len(str(stone))/2)]), int(str(stone)[int(len(str(stone))/2):])])
    else:
        return([stone*2024])
    
@cache
def blink(stone, n_times):
    if n_times == 1: return(len(apply_rules(stone)))
    else: 
        # 
        # This breaks my brain...
        # Why is the recursive blink iterating over the
        # processed ORIGINAL stone value?
        # 
        return(sum([blink(s, n_times-1) for s in apply_rules(stone)]))

def plutonian_stones(stones, n_times):
    return(sum([blink(s, n_times) for s in stones]))

part_1 = plutonian_stones(input, 25)
part_2 = plutonian_stones(input, 75)

### OLD CODE
from collections import defaultdict

def apply_rules(stone):
    if stone == 0:
        return([1])
    elif len(str(stone)) % 2 == 0:
        return([int(str(stone)[0:int(len(str(stone))/2)]), int(str(stone)[int(len(str(stone))/2):])])
    else:
        return([stone*2024])
    
def blink(stone, n_times):
    stones = {stone: 1}
    for i in range(0, n_times):
        temp_dict = defaultdict(int)
        for k, v in stones.items():
            new_val = apply_rules(k)
            for j in new_val: temp_dict[j] += v

        stones = temp_dict
    return(sum(stones.values()))

def plutonian_stones(stones, n_times):
    return(sum([blink(s, n_times) for s in stones]))

part_1 = plutonian_stones(input, 25)
part_2 = plutonian_stones(input, 75)