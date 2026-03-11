from math import*
angulo = radians(float(input("Digite angulo: ")))
velocidade_inicial = float(input("Digite velocidade: "))
g = 9.8 

d = ((velocidade_inicial**2) * (sin(2*angulo)))/g
print(round(d,2))