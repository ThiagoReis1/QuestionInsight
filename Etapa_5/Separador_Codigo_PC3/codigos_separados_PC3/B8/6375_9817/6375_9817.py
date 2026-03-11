from numpy import *
votos= input("Insira um candidato:").upper().split(",")
vet_new= zeros(4, dtype=int)


for i in votos:
	if i== "A":
		vet_new[0]= vet_new[0] + 1
	elif i== "B":
		vet_new[1]= vet_new[1] + 1
	elif i== "C":
		vet_new[2]= vet_new[2] + 1
	elif i== "D":
		vet_new[3]= vet_new[3] + 1
		
print(vet_new)
		