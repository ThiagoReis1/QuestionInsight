from math import*
q = float(input("quantos litros: "))
valor = (q*2.86) + 50
total = valor + valor*(34/100)
print(round(total, 2))