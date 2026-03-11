#Instituto de computação - UFAM
#Módulo 05 - Ex. 01
#10/08/2016
from numpy import *
vetor1 = array(eval(input("Informe as distancias obtidas nos saltos em metros:")))
record = 8.95


i = 0
salt = 0

while(i < size(vetor1)):
		salt = salt + i
		i = i + 1
print(record)
print(salt)