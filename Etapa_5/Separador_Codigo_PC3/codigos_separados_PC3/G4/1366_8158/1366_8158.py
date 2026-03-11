import math

ang = math.radians(float(input("digite o angulo: ")))
vo= float(input("digite a velocidade: "))
g = 9.8
d = (vo**2)*(math.sin(2*ang)/g)
print(round(d,2))
