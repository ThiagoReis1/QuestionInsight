from math import*

Vo = float(input("Velocidade inicial:"))
D  = float(input("Distância:"))

a = float(asin((D * 9.8) / (Vo**2)) * (90/pi))

print(round(a,2))