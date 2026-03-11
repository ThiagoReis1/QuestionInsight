from numpy import *

cabelo = input("digite: ").upper().split(',')
cont = zeros(5,dtype = int)

for i in range(size(cabelo)):
	if(cabelo[i] == 'P'):
		cont[0] = cont[0] + 1
	elif(cabelo[i] == 'C'):
		cont[1] =  cont[1] + 1
	elif (cabelo[i] == 'R'):
		cont[2] = cont[2] + 1
	elif(cabelo[i] == 'L'):
		cont[3] = cont[3] + 1
	elif (cabelo[i] == 'B'):
		cont = cont[4] + 1
print(cont)
