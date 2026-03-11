#av01 dia 16/06
#caio fernandes
from math import*
raio = float(input("digite o valor do raio: "))
area = pi*raio**2
custo = float(input("digite o custo do serviço: "))
tot = custo * area
print(round(tot,2))