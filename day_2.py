from functools import reduce
COLORS = ["red", "green", "blue"]


def line_parser(line):
    output = {
        'game_no': 0,
        'sets': []
    }
    res = line.split(':')
    output["game_no"] = int(res[0].replace('Game ', ''))
    sets = res[1].split(';')
    for st in sets:
        st_info = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        cubes_no = st.split(',')
        for cn in cubes_no:
            cn = cn.strip()
            for color in COLORS:
                if color in cn:
                    clean = cn.replace(color, '')
                    clean = clean.strip()
                    st_info[color] = int(clean)
        output["sets"].append(st_info)
    return output


max_count = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('day_2_input.txt', 'r', encoding='utf-8') as file:
    powers = []
    for line in file.readlines():
        # print(line.strip())
        game_info = line_parser(line)
        game_valid = True
        max_counts = {}
        for color in COLORS:
            max_counts[color] = max([st[color] for st in game_info["sets"]])
        print(max_counts)
        powers.append(reduce(lambda x, y: x*y, max_counts.values(),  1))
    print(sum(powers))
