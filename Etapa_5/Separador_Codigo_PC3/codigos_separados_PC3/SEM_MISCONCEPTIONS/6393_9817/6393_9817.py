from numpy import *
mensagem= array(eval(input("Insira um vetor mensagem:")))
vet_new= zeros(size(mensagem), dtype= int)

for i in range(size(mensagem)):
	if mensagem[i]== 9:
		vet_new[i]= 0** 3
	else:
		vet_new[i]= (mensagem[i] + 1) ** 3
		
print(vet_new)
		