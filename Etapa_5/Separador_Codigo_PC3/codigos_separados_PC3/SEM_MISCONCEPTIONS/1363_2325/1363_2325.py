"""
UNIVERSIDADE FEDERAL DO AMAZONAS
DISCENTE: Dave Monteiro Bonates   mat: 21601485
TURMA: Engenharia de Produção
DATA: 04/04/2017 
"""


p = float(input("Digite o valor em gramas da espada: "))
from math import*
#quantidade de flawless ruby necessária para o encantamento, em gramas.
flawless_ruby = 2**(1+p/1000)

#A quantidade de soul gem, em gramas.
soul_gem = p * pi**2/3141

#A quantidade de óleo de dwarven, em gramas.
oleo_dwarven = 2 * (p/40)**0.5

print(round(flawless_ruby,2))
print(round(soul_gem,2))
print(round(oleo_dwarven,2))