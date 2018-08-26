# Google Nil game
from functools import reduce
from operator import xor

piles = [0, 233, 232]

while True:
    # Users' turn
    for i in range(3):
        nim_sum = reduce(xor, piles)
        if (piles[i] ^ nim_sum) < piles[i]:
            coins = piles[i] - (piles[i] ^ nim_sum)
            print('stack', i + 1, 'coins', coins)
            piles[i] = piles[i] ^ nim_sum

    # Altrons' turn
    pile = int(input('stack: ')) - 1
    coins = int(input('coins: '))

    piles[pile] -= coins
