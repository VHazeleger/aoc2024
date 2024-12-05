with open('input.txt') as f:
    input = f.read().strip()

# parse data
rules, updates = input.split('\n\n')

rules = [tuple([int(x) for x in r.split('|')]) for r in rules.split('\n')]
updates = [[int(x) for x in u.split(',')] for u in updates.split('\n')]

# part 1
def check_update(update, rules):
    for r in rules:
        first, last = r[0], r[1]
        if first not in update or last not in update: continue
        if update.index(first) > update.index(last): return(0)
        
    return(1)

safe = []
unsafe = [] # part 2 prep
for u in updates:
    if check_update(u, rules) == 1: safe.append(u)
    else: unsafe.append(u) # part 2 prep

result = sum([s[int((len(s)-1)/2)] for s in safe])

# part 2
from collections import Counter
def fix_update(update, rules):
    # broken_rules = []
    while not check_update(update, rules):
        for r in rules:
            first, last = r[0], r[1]
            if first not in update or last not in update: continue
            if update.index(first) > update.index(last): 
                update[update.index(first)], update[update.index(last)] = update[update.index(last)], update[update.index(first)]

    return(update)

fixed = [fix_update(u, rules) for u in unsafe]
result2 = sum([s[int((len(s)-1)/2)] for s in fixed])