import random


def read_hands(filename:str) -> list[str]:
    '''
    Read list of sample hands from file
    '''
    with open(filename, encoding='utf-8') as f:
        return [x.strip().split(' # ') for x in f]


def main():
    '''
    Main function
    '''
    hands = read_hands('input1.txt')
  
    f = open('input2.txt', 'w', encoding='utf-8')

    # Write 20 random combination of two hands to output file
    for _ in range(20):
        i, j = random.sample(range(len(hands)), 2)
        f.write(f'{hands[i][0]}|{hands[j][0]} # {hands[i][1]}|{hands[j][1]}\n')

    f.close()


if __name__ == '__main__':
    main()