from math import*
ang=float(input("angulo:"))
vo=int(input("valor da velocidade:"))
g=9.8
d= vo**2*sin(radians(2*ang))/g

print(round(d,2))