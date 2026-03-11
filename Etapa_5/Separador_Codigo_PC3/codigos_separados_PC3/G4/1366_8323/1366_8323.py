from math import sin, radians
ang = float(input("De o angulo da flecha: "))
vel = float(input("De a velocidade inicial da flecha: "))
d = (vel**2) * (sin(2*radians(ang)))/9.8
print(round(d,2))