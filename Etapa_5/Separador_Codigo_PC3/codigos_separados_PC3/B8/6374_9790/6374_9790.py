from numpy import * 
pacientes = input("pacientes: ")
x = pacientes.split(",")
contO = 0
contD = 0
contN = 0
contC = 0
for i in x:
	if i == 'O':
		contO += 1
	elif i == 'D':
		contD += 1
	elif i == 'N':
		contN += 1
	elif i == 'C':
		contC += 1
cont = array([contO, contD, contN, contC])
print(cont)