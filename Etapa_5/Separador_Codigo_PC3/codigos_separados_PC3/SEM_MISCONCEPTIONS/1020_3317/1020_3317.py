from math import*
B = float(input("comprimento da base maior: "))
b = float(input("comprimento da base menor: "))
h = float(input("altura: "))
custoaplicacao = float(input("custo de aplicacao: "))
base = h * (B + b)/2
custo =  custoaplicacao * base
print(round(custo, 2))