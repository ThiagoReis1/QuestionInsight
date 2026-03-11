from math import*
ga = float(input("Quantidade de LT: "))



litro_gasolina = 2.86
troca_oleo = 50.00
imposto = 1.34
total = ((litro_gasolina * ga) + (troca_oleo)) * imposto

print(round(total,2))
