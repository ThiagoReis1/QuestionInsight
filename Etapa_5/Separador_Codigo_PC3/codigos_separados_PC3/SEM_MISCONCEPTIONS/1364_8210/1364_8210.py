from math import*
vi = float(input("Velocidade inicial: "))
d = float(input("Distancia: "))
angulo = asin(d*(9.8/(vi**2)))*(90/pi)
print(round(angulo,2))
