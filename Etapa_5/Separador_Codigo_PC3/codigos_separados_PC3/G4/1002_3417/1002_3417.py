from math import *
raio = float(input("digite o raio: "))
custo = float(input("digite o custo: "))
at = ((pi)*raio**2)
ct = at * custo

print(round(ct,2))