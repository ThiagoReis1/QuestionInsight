from numpy import *
estado = input("estados: ").split(',')
vet = len(estado)
i = 0 
soma = 0
while(i < vet):
	if(estado == "AM"):
		AM = AM + 1
		soma = AM + 1
	elif(estado == "PE"):
		PE = PE + 1
		soma = PE + 1
	elif(estado == "MG"):
		MG = MG + 1
		soma = MG + 1
	elif(estado == "SP"):
		SP = SP + 1
		soma = SP + 1
	elif(estado == "RS"):
		RS = RS + 1
		soma = RS + 1
	i = i + 1
print(max(soma))






#from numpy import *
#estado = input("estados: ").split(',')
#vet = len(estado)
#AM = 0
#PE = 0
#SP = 0
#RS = 0
#PE = 0
#MG = 0
#soma = 0
#for i in range(vet):
#	if(estado == "AM"):
#		AM = AM + 1
#		soma = soma + 1
#	elif(estado == "PE"):
#		PE = PE + 1
#		soma = soma + 1
#	elif(estado == "MG"):
#		MG = MG + 1
#		soma = soma + 1
#	elif(estado == "SP"):
#		SP = SP + 1
#		soma = soma + 1
#	elif(estado == "RS"):
#		RS = RS + 1
#		soma = soma + 1
#	print(soma)