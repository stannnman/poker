import random

def read_hands(filename):
    with open(filename) as f:
        return [x.strip().split(' # ') for x in f]



def main():
    hands = read_hands('input1.txt')
  
    f = open('input2.txt', 'w')
    for _ in range(20):
        i, j = random.sample(range(len(hands)), 2)

        f.write(f'{hands[i][0]}|{hands[j][0]} # {hands[i][1]}|{hands[j][1]}\n')

    f.close()









if __name__ == '__main__':
    main()