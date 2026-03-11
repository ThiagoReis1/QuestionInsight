from math import*
angulo=float(input("angulo:"))
vel=float(input("velocidade inicial:"))
ang=radians(angulo)
d=((vel**2)*((sin(2*ang))/9.8))
print(round(d,2))