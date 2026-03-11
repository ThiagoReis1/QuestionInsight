from math import *
preco_area = int(input("digite o preco por area: "))
p= float(input("digite o preco por areaP: "))
c = float(input("digite o preco por areaC: "))
g = float(input("digite o preco por areaG: "))
preco_total = float((p+c+g)*preco_area)
print(round(preco_total,2))