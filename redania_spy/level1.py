# ROT13
import string

ALPHABET = string.ascii_lowercase

text = """jzfnlyedezaldzwotpcqczxmptyrqctrsepypomfejzfnlyrtgpstx
xzetgletzyezspwastxzgpcnzxpesleqplctslgpyzdfnsxzetglet
zytnlyeslgptxlhtenspclylcetqtntlwwjncplepoxfelyet
vtwwxzydepcdqzcxzypjtopqpyonstwocpyhspyesptcalcpyedaljx
peztqytwqrllcotlyalcpyedaljxptwwopqpyoytwqrllcotlynstw
ocpylyopgpytqesphzcwowtpdtycftyhstnsozpdyzedppxwtvp
wjezxptwwnlccjzyvtwwtyrxzydepcdtyespcftydzqestdhzcw
ofyetwdzxpxzydepcvtwwdxpesletdxjqlepxjcpldzyxjwtqp
lyoxjleetefopezesphzcwolyotetdyzehsletnszdptehldns
zdpyqzcxplwwtnlyoztdszyzceszdphszaljxpeznlccjxjopp
odxlvtyrespxalddnzopdtdlwwtvyzhszhez"""


result = ''
for char in text.replace('\n', ''):
    result += ALPHABET[(ALPHABET.index(char) + 15) % 26]
print(result)
