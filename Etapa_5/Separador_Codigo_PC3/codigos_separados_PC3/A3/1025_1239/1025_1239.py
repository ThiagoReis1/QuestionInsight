#Instituo Federal do Amazonas.
#Avaliacao ICC
# 16 / 06 / 2016

from math import*
comprimento = float(input("Digite A: "))
largura = float(input("Digite a: "))
custo_m2 = float(input("Digite c: "))


A = comprimento
a = largura
c = custo_m2
p = custo_m2 * 2 * ( A + a )
print(round(p, 2))