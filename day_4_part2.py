from collections import namedtuple, deque
Card = namedtuple('Card', ['id', 'matches'])

with open('day_4_input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = [a.strip().replace('  ', ' ') for a in lines]
    all_cards = []
    mem = []
    for line in lines:
        res = line.split(':')
        id = int(res[0].replace('Card ', ''))
        res = res[1].split('|')
        win = set([int(x) for x in res[0].strip().split(' ')])
        have = set([int(x) for x in res[1].strip().split(' ')])
        matches = win.intersection(have)
        card = Card(id,  len(matches))
        all_cards.append(card)

    cards = deque(all_cards)

    total_count = 0

    while len(cards) > 0:
        cur_card = cards.popleft()
        card_index = int(cur_card.id)-1
        total_count += 1
        if cur_card.matches > 0:

            new_copies = all_cards[card_index+1: card_index+1+cur_card.matches]
            for nc in new_copies:
                cards.append(nc)

    print(total_count)
