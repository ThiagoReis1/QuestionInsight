q = float(input("Quantidade de litros abastecidos: "))

v1 = (q * 2.86) + 50
v2 = v1 * 0.34

vt = v1 + v2

print(round(vt, 2))