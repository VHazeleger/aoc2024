with open('input.txt') as f:
    input = f.read().strip()

example = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()

# parse data
input = [[int(y) for y in x.split(' ')] for x in input.split('\n')]

# part 1
def check_safety(report):
    if report[1] - report[0] > 0:
        asc = True 
    elif report[1] - report[0] < 0:
        asc = False
    else:
        return(0)
    for idx, val in enumerate(report):
        if idx == 0: continue
        
        if asc and not 0 < val - report[idx-1] <= 3: return(0)
        if not asc and not 0 > val - report[idx-1] >= -3: return(0)
    
    return(1)

safe=0
for report in input:
    safe += check_safety(report)

# part 2
unsafe_reports = [r for r in input if check_safety(r) == 0]
ur_safe = 0
for ur in unsafe_reports:
    for i in range(0, len(ur)):
        copy_ur = ur[:]
        del copy_ur[i]
        if check_safety(copy_ur) == 1:
            ur_safe += 1
            break

result = safe + ur_safe

