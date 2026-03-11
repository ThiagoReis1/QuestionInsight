from math import *

# preco da passagem
preco = float(input("p: "))

# passagem do acompanhante
pa = float(input("pa: "))

#desconto 
pac = pa - (pa * 35 / 100)

# som das passagemns
soma = preco + pac 

print(round(preco, 2))
print(round(pac, 2))
print(round(soma, 2))
