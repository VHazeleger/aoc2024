with open('input.txt') as f:
    input = f.read().strip()

# parse data
left = []
right = []

input_split = [tuple(x.split('   ')) for x in input.split('\n')]

for l, r in input_split:
    left.append(int(l))
    right.append(int(r))
    
left.sort()
right.sort()

# part 1
result_1 = sum([abs(x) for x in [l - r for l, r in zip(left, right)]])

# part 2
from collections import Counter

occurrences_r = Counter(right)

result_2 = sum([n * occurrences_r[n] for n in left])