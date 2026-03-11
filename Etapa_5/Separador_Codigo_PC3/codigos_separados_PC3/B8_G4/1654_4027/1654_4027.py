from numpy import *
string = input("Insira a string contendo as siglas dos estados: ")
string = string.split(',')
vet = zeros(5, dtype = int)
n = size(string)
AM = 0
PE = 0
MG = 0
SP = 0
RS = 0
for i in range(n):
	if(string[i] == "AM"):
		AM = AM + 1
	elif(string[i] == "PE"):
		PE = PE + 1
	elif(string[i] == "MG"):
		MG = MG + 1
	elif(string[i] == "SP"):
		SP = SP + 1
	elif(string[i] == "RS"):
		RS = RS + 1
vet[0] = AM
vet[1] = PE
vet[2] = MG
vet[3] = SP
vet[4] = RS

print(max(vet))
print(vet)