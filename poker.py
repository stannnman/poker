from collections import namedtuple, Counter


Card = namedtuple("Card", "num suit")
card_nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

hand_values = [
    'nothing',
    'two of a kind',
    'two pair',
    'three of a kind',
    'straight',
    'flush',
    'full house',
    'poker',
    'straight flush',
    ]


def read_games(filename:str) -> list[str]:
    with open(filename, encoding='utf-8') as f:
        return [x.strip() for x in f]


def get_cards(hand:str) -> list[Card]:
    return [Card(h[:-1], h[-1]) for h in hand.split(',')]


def sort_cards(cards:list[Card]) -> list[Card]:
    return sorted(cards, key=lambda x: card_nums.index(x.num))


def get_hand_value(cards:list[Card]) -> str:
    nums_counter = Counter([card.num for card in cards])
    suits_counter = Counter([card.suit for card in cards])

    most_common = nums_counter.most_common(2)
    most_common1 = most_common[0][1]
    most_common2 = most_common[1][1]

    if most_common1 == 4:
        return 'poker'

    if most_common1 == 3:
        if most_common2 == 2:
            return 'full house'
        else:
            return 'three of a kind'

    if most_common1 == 2:
        if most_common2 == 2:
            return 'two pair'
        else:
            return 'two of a kind'

    # Add an Ace at the start to allow a straight of A1234
    card_nums_plus = ['A'] + card_nums

    straight = card_nums_plus.index(cards[4].num) \
        - card_nums_plus.index(cards[0].num) == 4

    flush = len(suits_counter) == 1
    
    if straight:

        if flush:
            if cards[0].num == '10':
                return 'royal flush'
            else:
                return 'straight flush'
        else:
            return 'straight'

    if flush:
        return 'flush'

    return 'nothing'


def main():
    games = read_games('input2.txt')

    for game in games:
        print(game)
        hands = game.split(' # ')[0]
        hand1, hand2 = hands.split('|')

        cards1 = sort_cards(get_cards(hand1))
        cards2 = sort_cards(get_cards(hand2))

        hand_value1 = get_hand_value(cards1)
        hand_value2 = get_hand_value(cards2)

        index1 = hand_values.index(hand_value1)
        index2 = hand_values.index(hand_value2)

        if index2 > index1:
            result = 'Two wins'
        elif index1 > index2:
            result = 'One wins'
        else:
            result = 'Draw'

        print(f'{result}\n')


if __name__ == '__main__':
    main()