from math import*

valor = float(input("valor da encomenda"))
imposto = (valor*81/100) + 12
total = valor + imposto

print(round(total, 2))
