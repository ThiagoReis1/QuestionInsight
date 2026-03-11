from math import *
arv = float(input("Digite a estimativa de árvores: "))
a = float(input("Digite comprimento do lado da região pentagonal de floresta: "))
area = (a**2*(sqrt(25+10*sqrt(5))))/4
total = area*arv
print(int(total))