# Vigenere
import string
from itertools import cycle

ALPHABET = string.ascii_lowercase

text = """
oqrnlzkfvclnyizhlokxfbpvgyjetokrfoeakvnajhaxsentawvigxuzvrnh
sikhpogrztjtthgrtwkswbpbtkuiqykvvnebbilnoxxwkozwzlrteakcrrpt
vmkiqnrhvfpgyirglbtwkbpbtkuiqykvvneukgrudxozvuywkvjtzhjxyaem
nijuylnmeedwojwecxtxcyhakrjoxxzlznrvneegplhykixguxkhptdmjoqm
nsjenagrxedmnijuylnmeedwojwecxtxcymnzmkwtergfnebtyvtzlnmeelg
jnlmabtkrttmcmkhlauizsymmsznrmuhfayrzlznrpkzvgzmzsrcnxvxwanm
yicfeagxjwstzavvpzuxkowxgvetsxvejshhxhzsdtvofwddo
""".strip().replace('\n', '')

key = 'geralt'
key = [ALPHABET.index(char) for char in key]

result = ''
for char, shift in zip(text, cycle(key)):
    result += ALPHABET[(ALPHABET.index(char) - shift)]

print(result)
