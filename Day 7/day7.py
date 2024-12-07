with open('input.txt') as f:
    input = f.read().strip()

example = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''.strip()

# input = example

from itertools import product

def fill_in(numbers, operators):
    calc = []
    for n in range(len(operators)):
        calc.append(numbers[n])
        calc.append(operators[n])
    calc.append(numbers[n+1])
    return(calc)

def eval_ltr(operation):
    first = operation.pop(0)
    while(len(operation) > 0):
        operator = operation.pop(0)
        second = operation.pop(0)
        if operator == '||':
            temp_result = str(first)+second
        else:
            temp_result = eval(f'{first}{operator}{second}')
        first = int(temp_result)
    return(int(temp_result))

def run(input = input, ops = ['*', '+']):
    result = 0
    for r in input.split('\n'):
        # print(r)
        bignum, parts = r.split(': ')
        bignum = int(bignum)
        parts = parts.split(' ')
        c_p = product(ops, repeat=len(parts)-1)

        for operators in c_p:
            operation = fill_in(parts, operators)
            # print(operation)
            
            if eval_ltr(operation) == bignum:
                # print(operation, bignum)
                result += bignum
                break
    return(result)

# part_1 = run()
part_2 = run(input, ['*', '+', '||'])