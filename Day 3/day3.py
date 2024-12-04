with open('input.txt') as f:
    input = f.read().strip()

# part 1
import regex as re

muls = re.findall('mul\(\d+,\d+\)', input)

def mul(a, b):
    return(a*b)

sum = 0
for m in muls:
    sum += eval(m)

# part 2
valid = ''
remainder = input
while "don't" in remainder:    
    valid += remainder.split("don\'t()", 1)[0]
    remainder = remainder.split("don\'t()", 1)[1]
    remainder = remainder.split("do()", 1)[1] 
    
valid += remainder

muls2 = re.findall('mul\(\d+,\d+\)', valid)

sum2 = 0
for m in muls2:
    sum2 += eval(m)
