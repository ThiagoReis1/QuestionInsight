from math import*
varraio = float(input("qual o raio?"))
varlados = int(input("numero de lados?"))
varA = (1/2*((varraio*cos(pi/varlados))**2*tan(pi/varlados)))
print(round(varA,2))