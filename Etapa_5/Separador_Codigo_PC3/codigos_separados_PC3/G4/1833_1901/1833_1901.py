from math import*
ma=int(input("Massa do caminhão A:"))
mb=int(input("Massa do Caminhão B:"))
Vob=int(input("Velocidade do caminhão B:"))
vel_final=((2*ma+mb)/(ma+mb))*Vob
print(vel_final)