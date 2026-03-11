from math import *
ladob = float(input("Inserir cateto oposto: "))
ladoc = float(input("inserir cateto adjacente: "))
ang = (radians(float(input("inserir angulo: "))))

x = sqrt((ladob**2+ladoc**2)-(2*ladob*ladoc)*cos(ang))
print(round(x,2))