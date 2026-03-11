from math import*
kw = float(input("digite o valor de kwh consumido neste mes:"))
conta = kw*0.43 + 10
total = conta + conta*0.25
print(round(total, 2))


