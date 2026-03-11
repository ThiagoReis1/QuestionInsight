v0=float(input("Digite um valor: "))
d=float(input("Digite um outro valor: "))
g=9.8
from math import*
ang=asin(d*g/v0**2)*90/pi
print(round(ang,2))
