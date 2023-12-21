from collections import namedtuple

Mapp = namedtuple('Mapp', ["dest", "source", "range"])


def get_next(start_val, map_list):
    result = None
    for mp in map_list:
        if start_val >= mp.source and start_val < mp.source+mp.range:
            result = start_val + (mp.dest - mapp.source)
    if result is None:
        result = start_val
    return result


with open('day_5_input.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    maping = {}
    sections = content.split('\n\n')
    for sec in sections:
        res = sec.split(':')
        name = res[0].strip().replace(' map', '')
        data = res[1].strip().split('\n')
        if name == "seeds":
            data = data[0].strip().split(' ')
            maping[name] = [int(x) for x in data]
        else:
            connections = []
            for d in data:
                dline = d.split(' ')
                dline = [int(x) for x in dline]
                mapp = Mapp(*dline)
                connections.append(mapp)
            maping[name] = connections
    vals = []

    seed_list_total = []
    for idx in range(0, len(maping["seeds"]), 2):
        seed_list = range(maping["seeds"][idx],
                          maping["seeds"][idx] + maping["seeds"][idx+1])
        seed_list_total += seed_list
    for rng in seed_list_total:
        for seed in rng:
            # TODO: there must be something in python functools to
            # make this nicer
            next_val = get_next(seed, maping['seed-to-soil'])
            next_val = get_next(next_val, maping['soil-to-fertilizer'])
            next_val = get_next(next_val, maping['fertilizer-to-water'])
            next_val = get_next(next_val, maping['water-to-light'])
            next_val = get_next(next_val, maping['light-to-temperature'])
            next_val = get_next(next_val, maping['temperature-to-humidity'])
            next_val = get_next(next_val, maping['humidity-to-location'])
            vals.append(next_val)
    print(min(vals))
