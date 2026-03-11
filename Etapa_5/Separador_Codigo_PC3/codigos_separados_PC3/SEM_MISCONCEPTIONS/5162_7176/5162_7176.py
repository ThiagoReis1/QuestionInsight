import math
e = float(input("estimativa de acaizeiros: "))
a = float(input("comprimento da aresta: "))
qtd_total = e * 3 *(math.sqrt(3*a**2)/2)
print(int(qtd_total))