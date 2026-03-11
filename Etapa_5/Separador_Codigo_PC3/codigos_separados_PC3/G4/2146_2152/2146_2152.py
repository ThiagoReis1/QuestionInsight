from numpy import *

vet = input("digita  ae: ")
zet = ""
for i in range(len(vet)):
	if(vet[i].isupper()):
		zet = zet + vet[i].lower()
	else:
		zet = zet + vet[i].upper()
print(zet)