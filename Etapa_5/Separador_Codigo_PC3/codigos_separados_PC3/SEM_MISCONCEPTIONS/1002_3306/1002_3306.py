from math import*
#raio aproximado em metros
raio=float(input("digite o valor do raio:"))
#custo de fertilizante por metro quadrado
custo= float(input("digite o valor por m2:"))
#area
area= (pi)*(raio**2)
custototal= area*custo
print(round(custototal, 2))