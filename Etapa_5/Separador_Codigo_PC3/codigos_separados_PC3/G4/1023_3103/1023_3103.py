from math import*
a = float(input("Qual o valor do raio ?: "))
custo = float(input("Qual o custo de construcao da cerca por metro ?: "))
Pc = 2 * pi * a
Tc = Pc * custo
print(round(Tc,2))