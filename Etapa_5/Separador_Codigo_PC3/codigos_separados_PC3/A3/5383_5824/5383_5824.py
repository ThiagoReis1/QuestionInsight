from numpy import *
nome=input("Nome:").upper()
ind= 0
total=0
vogal=("A","E","I","O","U")
while ind<size(nome): 

	if nome==vogal:
		total=nome[ind]*0.12
	
	else: total=nome[ind]*0.18
	ind=ind+1
print(total)
		