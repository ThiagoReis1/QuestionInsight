from math import*

q = float(input("digite a quantidade de litros:"))

custo_total = (((2.86 * q) + 50) * (34 / 100)) + ((2.86 * q) + 50) 

print(round(custo_total, 2))