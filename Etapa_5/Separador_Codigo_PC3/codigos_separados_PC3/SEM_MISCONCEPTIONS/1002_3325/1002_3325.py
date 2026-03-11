from math import*
raio = float(input("digite o valor da area"))
custo = float(input("custo por metro quadrado"))

custoT = pi * (raio)**2 * custo
print(round(custoT,2))