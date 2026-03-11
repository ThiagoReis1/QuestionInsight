from numpy import*
from math import*

etnia = input("digite sua etnia:").split(',')

vet_final = zeros(5,dtype = int)

cont_Branco = 0;
cont_Pardo = 0;
cont_Preto = 0;
cont_Amarelo = 0;
cont_Indigena = 0;
j= 0;
for i in etnia:
	if(i == "B"):
		cont_Branco += 1;
		vet_final[j] += 1;
	elif(i == "PA"):
		cont_Pardo += 1;
		vet_final[j] += 1;
	elif(i == "A"):
		cont_Amarelo += 1;
		vet_final[j] += 1;
	elif(i == "PR"):
		cont_Preto += 1;
		vet_final[j] += 1;
	elif(i == "I"):
		cont_Indigena += 1;
		vet_final[j] += 1;
	j += 1;	
print(vet_final)
