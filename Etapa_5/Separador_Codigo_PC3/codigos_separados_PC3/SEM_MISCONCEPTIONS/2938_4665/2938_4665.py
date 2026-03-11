from math import*
distanciaa = float(input("Qual a distancia?"))
distanciab = float(input("Qual a distancia?"))
angulo = radians(float(input("Qual o angulo?")))
total = sqrt(distanciaa**2+distanciab**2-2*distanciaa*distanciab*cos(angulo))
print(round(total,2))