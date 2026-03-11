from math import*

round(float(input("comprimento do cateto_1:")))
round(float(input("comprimento do cateto_2:")))
round(float(input("custo:")))

cateto_a = 100
cateto_b = 200
custo = 4.35

area_do_triangulo = cateto_a * cateto_b / 2

custo_total = area_do_triangulo * custo

print(custo_total ** 2)