from math import sin, radians
angulo=float(input(" o angulo da flesha deve ser em graus"))
velocidade=float(input(" a velocidade deve ser em metros por segundo"))
g=9.8
distancia=(velocidade**2)*(sin(2*radians(angulo))/g)
print(round(distancia,2))