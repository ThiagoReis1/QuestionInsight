from numpy import *

#vet = ones(10, dtype=int)
#cont = 0
#while cont < 10:
#	vet[cont] = int(input())
#	cont += 1
#
#num = int(input())
#
#cont = 0
#for i in vet:
#	if i >= num:
#		cont += 1
#		
#listVet = vet.split("")
#vetaux = "[ "
cont = 0
teste = ""
while cont < 10:
	num = input()
	teste += num + " "
listT = teste.split(" ")
#print (cont)
print (listT)
