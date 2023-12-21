"""
nadjemo svaki broj
i pamtimo coords
    row[0],span[0,2]
i onda pustimo scouta koji ide okolo
    clockwise i ako nadje symbol, break i dodaj broj
"""

import re

part_numbers = []


with open('day_3_input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = [a.strip() for a in lines]
    for idx, row in enumerate(lines):
        numbers = re.finditer('\d+', row)
        for n in numbers:
            num_info = {
                'num': n.group(),
                'row': idx,
                'span': [n.span()[0], n.span()[1]-1]
            }
            part_numbers.append(num_info)
    matrix = [list(l) for l in lines]
    out = 0
    for pt_no in part_numbers:
        pt_no["valid"] = False
        to_visit = []
        row_indexes = []
        col_indexes = []
        if pt_no['row']-1 >= 0:
            row_indexes.append(pt_no['row']-1)
        if pt_no['row']+1 <= (len(matrix)-1):
            row_indexes.append(pt_no['row']+1)
        for c in range(pt_no['span'][0]-1, pt_no['span'][1]+2):
            if c >= 0 and c <= len(matrix[0])-1:
                col_indexes.append(c)
        for r in row_indexes:
            for c in col_indexes:
                to_visit.append((r, c))
        # left and right
        if pt_no['span'][0]-1 >= 0:
            to_visit.append((pt_no["row"], pt_no['span'][0]-1))
        if pt_no["span"][1]+1 <= len(matrix[0])-1:
            to_visit.append((pt_no["row"], pt_no["span"][1]+1))
        for point in to_visit:
            val = matrix[point[0]][point[1]]
            if not val.isdigit() and val != '.':
                pt_no["valid"] = True

    print(sum([int(p["num"]) for p in part_numbers if p["valid"]]))
