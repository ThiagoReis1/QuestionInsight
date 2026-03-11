from math import*

raio = float(input("qual a medida do bolt: "))
custo = float(input("qual o valor: "))

areadocirculo = pi * raio ** 2

precodarea = areadocirculo * custo

print(round(precodarea, 2))