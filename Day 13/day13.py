with open('input.txt') as f:
    input = f.read().strip()

# parse
machines = [m.split('\n') for m in input.split('\n\n')]   

def do_math(m, part2 = False):
    add = 0
    if part2:
        add = 10000000000000

    A = (int(m[0].replace('Button A: ','').split(', ')[0].replace('X+', '')), int(m[0].replace('Button A: ','').split(', ')[1].replace('Y+', '')))
    B = (int(m[1].replace('Button B: ','').split(', ')[0].replace('X+', '')), int(m[1].replace('Button B: ','').split(', ')[1].replace('Y+', '')))
    P = (int(m[2].replace('Prize: ','').split(', ')[0].replace('X=',''))+add, int(m[2].replace('Prize: ','').split(', ')[1].replace('Y=', ''))+add)

    

    valB = (P[1] * A[0] - A[1] * P[0]) / (B[1] * A[0] - A[1] * B[0])
    valA = (P[0] - B[0] * valB) / A[0]

    if valA % 1 == 0.0 and valB % 1 == 0.0:
        return(int(3*valA + valB))
    else: return(0)

part_1 = sum([do_math(m) for m in machines])
part_2 = sum([do_math(m, part2=True) for m in machines])