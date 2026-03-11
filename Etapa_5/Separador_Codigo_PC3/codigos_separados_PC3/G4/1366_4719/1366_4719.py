from math import*
ang = radians(float(input("angulo")))
velo = float(input("velocidade: "))
d = (velo**2*sin(2*ang))/9.8
print(round(d, 2))