from math import *

a = float(input("insira o comprimento em metros: "))
custoAp = float(input("insira o custo de aplicacao: "))

area = (2*(a**2)*((sqrt(2)) + 1))

custo_tot = custoAp * area
print(round(custo_tot,2))