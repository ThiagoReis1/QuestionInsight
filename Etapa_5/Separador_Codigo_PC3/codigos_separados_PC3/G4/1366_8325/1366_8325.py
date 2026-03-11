import math
ang=float(input("angulo: "))
v=float(input("velocidade: "))
g=9.8
print(round(v**2*(math.sin(math.radians(2*ang))/g),2))