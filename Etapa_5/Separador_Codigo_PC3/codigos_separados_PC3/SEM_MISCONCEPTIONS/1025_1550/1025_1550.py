from math import *
A = float(input("digite a largura:"))
a = float(input("digite o comprimento:"))
c_de_const = float(input("digite o custo de construção:"))
round(c_de_const,2)
p = 2*(A + a)
c_total= (c_de_const*p)
print(round(c_total,2))