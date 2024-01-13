# strength = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2"
# five of kind, four of kind, full house, three of kind, two pair, one pair, high card
# 5, 41, 32, 311, 221, 2111, 11111
# 5, 41, 32, 31, 22, 21, 11
# 6, 5, 4, 3, 2, 1, 0

from audioop import reverse

with open('07_task02.txt') as f:
    task = f.read()
    
card_letters_dictionary = {
    'A': 'F',
    'K': 'D',
    'Q': 'C',
    'J': 'B',
    'T': 'A'
}

rank_dictionary = {
    5: 7,
    41: 6,
    32: 5,
    311: 4,
    221: 3,
    2111: 2,
    11111: 1
}

# create extra column with mapped card letters to allow correct sort order
def map_card_letters(hand: str):
    return ''.join(str(card_letters_dictionary.get(char, char)) for char in hand)

# function to find order of strength
def order_of_strength(hand: str):
    kind_dictionary = {}
    for kind in hand:
        kind_dictionary[kind] = kind_dictionary.get(kind, 0) + 1
    rank = int("".join(map(str, sorted(list(kind_dictionary.values()), reverse=True))))
    return rank_dictionary.get(rank)

hands = list(task.splitlines())
strengths = set()

# iterate over the list to enrich it with order of strength
for i in range(len(hands)):
    hands[i] = hands[i].split(" ")
    hands[i].append(order_of_strength(hands[i][0]))
    hands[i].append(map_card_letters(hands[i][0]))
    strengths.add(hands[i][2]) # log what strengths we have in our hands

# define the maximum possible rank
current_rank = len(hands)
hands_enriched = []

# loop in a loop: first is a loop over type by priority, second is a loop based on sorted elements
for i in sorted(list(strengths), reverse=True):
    filtered_list = []
    filtered_list = [sublist for sublist in hands if sublist[-2] == i]
    filtered_list.sort(key=lambda x: x[3], reverse=True)
    for j in range(len(filtered_list)):
        filtered_list[j].append(current_rank)
        current_rank -= 1
    hands_enriched.extend(filtered_list)

# iterating and multiplying
total_winnings = 0
for i in range(len(hands_enriched)):
    # print(hands_enriched[i]) # for troubleshooting and visual control only
    total_winnings += int(hands_enriched[i][1]) * hands_enriched[i][4]
    
print(total_winnings)
