from math import sqrt
a = float(input("digite o valor da aresta:"))
area = (3*sqrt(3))*(a**2)/2
c = float(input("digite o custo por m2:"))
custo_total = area*c
custo_total = round(custo_total, 2)
print (custo_total)
        