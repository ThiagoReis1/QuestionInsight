math import*
angulo = float(input(radians("angulo da flexa: ")))
d = int(input("distancia em metros: "))
v0 = sqrt(d*(g/ sin (2*angulo)))
print(round(v0, 2))
