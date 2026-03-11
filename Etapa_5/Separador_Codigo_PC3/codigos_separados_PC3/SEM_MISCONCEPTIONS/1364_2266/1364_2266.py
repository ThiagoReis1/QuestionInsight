from math import*
g = 9.8

v = float(input("Qual a velocidade inicial da flecha? "))
d = float(input("Qual a distância até o alvo? "))
arcoseno = asin(d*g/(v**2))
ang = arcoseno*(90/pi)
angulo = ang
print (round(angulo,2))