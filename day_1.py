from pathlib import Path
import re

char_nums = 'one, two, three, four, five, six, seven, eight, nine'
nums = [n for n in range(1, 10)]
char_nums = char_nums.split(', ')
lens = set([len(c) for c in char_nums])
map = dict(zip(char_nums, nums))


wd = Path(r"D:\pajtoni\advent_of_code_2023")
real = 'day_1_input.txt'
test = 'test.txt'
with open(wd/real, 'r', encoding='utf-8') as file:
    arr = []
    for line in file.readlines():
        line = line.strip()
        # idem char po char i liniji
        # ako sve posle char ima i dict zamenim
        # ako nema idem dalje
        replacements = []
        # store replacements in a list and then iterate through it
        stack = ""
        for char in line:
            if char.isdigit():
                replacements.append(int(char))
                stack = ""
            else:
                stack += char
                if stack in map:
                    replacements.append(map[stack])
                for idx, ch in enumerate(stack):
                    span = stack[idx:]
                    if span in map:
                        replacements.append(map[span])
        print(f"{replacements[0]}{replacements[-1]}")
        arr.append(int(f"{replacements[0]}{replacements[-1]}"))

    print(sum(arr))
