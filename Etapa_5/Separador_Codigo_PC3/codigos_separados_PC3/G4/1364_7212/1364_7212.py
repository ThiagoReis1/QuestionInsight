from math import*
vo= float(input("velocidade inicial"))
d= float(input("distancia"))
g=9.8
a= asin(d*(g/vo**2))* 90/pi
print(round(a,2))