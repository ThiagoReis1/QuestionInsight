from math import*
minutos = float(input())
fixo = 23.00
custo = minutos * 0.28
total = custo + fixo
imposto = total + total * (31 / 100) 
print(round(imposto, 2))