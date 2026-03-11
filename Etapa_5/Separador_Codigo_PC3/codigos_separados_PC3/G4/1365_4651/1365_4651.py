from math import*

a=radians(float(input("Digite o angulo em graus: ")))
d=float(input("Digite a distancia em metros: "))

v0=sqrt(d*(9.8/sin(2*a)))

print(round(v0,2))