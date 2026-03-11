from math import*
a = float(input("Qual a distancia do stick ate a arvore A?"))
b = float(input("Qual a distancia do stick ate a arvore B?"))
gama = float(input("Qual o angulo em graus entre A e B?"))
cos_de_gama = cos(radians(gama))
c = sqrt(a**2+b**2-2*a*b*cos_de_gama)
print(round(c, 2))
