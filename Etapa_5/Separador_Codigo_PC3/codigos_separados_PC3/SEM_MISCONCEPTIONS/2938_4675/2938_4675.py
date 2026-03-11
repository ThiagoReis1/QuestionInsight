from math import*
dist1 = float(input("distancia da arvore a:"))
dist2 = float(input("distancia da arvore b"))
ang = radians(float(input("angulo entre a e b:")))
dist = sqrt(dist1**2+dist2**2-2*dist1*dist2*cos(ang))
print(round(dist,2))