with open('input.txt') as f:
    input = f.read().strip()

example = '2333133121414131402'

def convert_to_block_list(input = input):
    block_list = []
    file_id = 0
    for idx, d in enumerate(input):
        d = int(d)        
        if idx % 2 == 0: 
            block_list += [file_id] * d
            file_id += 1
        else:
            block_list += ['.'] * d
    return(block_list)

def order(input = input):
    remainder = convert_to_block_list(input)
    while '.' in remainder:
        last_num = remainder.pop()
        if last_num == '.': continue
        remainder[remainder.index('.')] = last_num

    return(remainder)

def checksum(ordered_input):
    result = 0
    for idx, i in enumerate(ordered_input):
        if i == '.': continue
        result += idx*i
    return(result)

ex_part_1 = checksum(order(example))
part_1 = checksum(order(input))

# part 2
import numpy as np

def find_gap(block_list, size):
    # temp = ''.join([str(x) for x in block_list]) # does not work with file ID > 9
    temp = [block_list[idx: idx + size] == ['.']*size for idx in range(len(block_list) - size + 1)]
    if True in temp:
        return(temp.index(True))
    return(-1)

def file_id_slice(block_list_np, file_id):
    indices = np.where(block_list_np==str(file_id))[0].tolist()
    return((indices[0], indices[-1]+1))

def order2(input = input):
    block_list = convert_to_block_list(input)
    block_list_np = np.array(block_list)
    for id in range(int(max([str(x) for x in block_list])), 0, -1):
        file_id_indices = file_id_slice(block_list_np, id)
        blocks = block_list[file_id_indices[0]:file_id_indices[1]]
        gap = find_gap(block_list[:file_id_indices[0]], len(blocks))
        if gap == -1: continue
        block_list[gap:gap+len(blocks)], block_list[file_id_indices[0]:file_id_indices[1]] = block_list[file_id_indices[0]:file_id_indices[1]], block_list[gap:gap+len(blocks)]
    return(block_list)

ex_part_2 = checksum(order2(example))
part_2 = checksum(order2(input))
