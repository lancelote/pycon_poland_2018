import pandas as pd
import matplotlib.pyplot as plt

# from string import ascii_uppercase
#
# ALPHABET = ascii_uppercase

TEXT = """
HDRFSFBFHFCDDEEFOAZFOEBAYASBKCZBHCFHHGNDZG
NCVEIAXADGBEBDCEOCEALHKHEBXBVGVDKEUAGBVFSG
AFDHXEIHGCKAOGTAAGREXCOBGFWADDDBTHOFQBDCPA
ZEXDLAHAEDNERCGHZADFKGGABHZHAEACGESCKBGDHE
MGAHSAUHNFAATDBBVBADODDAXHSHMBPHSEHBHHTEAB
VHVAEHZDOHKFBCECGGXGRDKDZCXFEGEEVCQGFABGSD
""".strip().split('\n')


# result = ''
#
# for i in range(len(TEXT)//2):
#     first = TEXT[i*2]
#     second = TEXT[i*2 + 1]
#     new = ALPHABET[(ALPHABET.index(first) + ALPHABET.index(second)) % 26]
#     result += new
#
# print(result)
# print(len(result))


lines = []

for line in TEXT:
    lines.append(''.join(format(ord(char), 'b') for char in line))

# for i in range(len(TEXT[0])):
#     line = ''
#     for j in range(len(TEXT)):
#         line += TEXT[j][i]
#     lines.append(''.join(format(ord(char), 'b') for char in line))

for line in lines:
    print(line.replace('0', ' ').replace('1', '#'))
