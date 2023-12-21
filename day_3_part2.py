import re
from functools import reduce

part_numbers = []
gears = []
row_map = {}


#koristiti neke named tuple
#koristiti neke generatore ako nesto iteriram jednom
#kako da imam default polje u dict?


def get_points_to_visit(element, matrix):
    '''
    vraca listu pointa(x,y) koordinata u matrixu koje treba da
    posetimo oko elementa
    '''
    to_visit = []
    row_indexes = []
    col_indexes = []
    if element['row']-1 >= 0:
        row_indexes.append(element['row']-1)
    if element['row']+1 <= (len(matrix)-1):
        row_indexes.append(element['row']+1)
    for c in range(element['span'][0]-1, element['span'][1]+2):
        if c >= 0 and c <= len(matrix[0])-1:
            col_indexes.append(c)
    # top and bottom row
    for r in row_indexes:
        for c in col_indexes:
            to_visit.append((r, c))
    # left and right
    if element['span'][0]-1 >= 0:
        to_visit.append((element["row"], element['span'][0]-1))
    if element["span"][1]+1 <= len(matrix[0])-1:
        to_visit.append((element["row"], element["span"][1]+1))
    return to_visit


with open('day_3_input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = [a.strip() for a in lines]
    id = 0
    for idx, row in enumerate(lines):
        numbers = re.finditer('\d+', row)
        for n in numbers:
            id += 1
            num_info = {
                'id': id,
                'num': n.group(),
                'row': idx,
                'span': [n.span()[0], n.span()[1]-1]
            }

            part_numbers.append(num_info)
        stars = re.finditer('\*', row)
        for star in stars:
            star_info = {
                'row': idx,
                'span': [star.span()[0], star.span()[1]-1]
            }
            gears.append(star_info)
    matrix = [list(l) for l in lines]
    for pt_no in part_numbers:
        pt_no["valid"] = False
        to_visit = get_points_to_visit(pt_no, matrix)
        for point in to_visit:
            val = matrix[point[0]][point[1]]
            if not val.isdigit() and val != '.':
                pt_no["valid"] = True
                if pt_no["row"] not in row_map:
                    row_map[pt_no["row"]] = []
                row_map[pt_no["row"]].append(pt_no)

    for gear in gears:
        touched_numbers = []
        touched_ids = []
        to_visit = get_points_to_visit(gear, matrix)
        for point in to_visit:
            x, y = point
            if x in row_map:
                candidates = row_map[x]
                for cand in candidates:
                    if y in range(cand["span"][0], cand["span"][1]+1):
                        if cand["id"] not in touched_ids:
                            touched_numbers.append(int(cand["num"]))
                            touched_ids.append(cand["id"])
        if len(touched_numbers)>1:
            gear["ratio"] = reduce(lambda x, y: x*y, touched_numbers, 1)
        else:
            gear["ratio"] = 0
    # That's not the right answer; your answer is too high.
    print(sum([g["ratio"] for g in gears]))
