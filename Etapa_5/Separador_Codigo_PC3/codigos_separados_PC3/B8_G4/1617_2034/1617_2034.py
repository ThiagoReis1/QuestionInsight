from numpy import*
vet=array(eval(input('Digite o tipo de espada:'))).split(",")
vet2= array(eval(input('Digite numeros inteiros:')))
dano=0
for i in range(size(vet)):
	if(vet[i]=="CENOURA"):
		dano= dano + 2*vet2[i]
	elif(vet[i]=="FERRO"):
		dano= dano + 4*vet2[i]
	elif(vet[i]=="DWARVEN"):
		dano=dano +8*vet2[i]
	elif(vet[i]=="ELVEN"):
		dano=dano+ 11*vet2[i]
	elif(v[i]=="DAEDRIC"):
		dano=dano+ 14*vet2[i]
print(int(dano))		