#Lucas Nascimento Estevam da Silva		21602757
#Prova Final
#Exercicio 02

from numpy import*

vet = input("Estados: ").split(',')
final = zeros(5, dtype= int)

for i in range(size(vet)):
	if(vet[i] == 'AC'):
		final[0] = final[0] + 1
	elif(vet[i] == 'AM'):
		final[1] = final[1] + 1
	elif(vet[i] == 'PA'):
		final[2] = final[2] + 1
	elif(vet[i] == 'RO'):
		final[3] = final[3] + 1
	elif(vet[i] == 'RR'):
		final[4] = final[4] + 1
		
maior = max(final)
print(maior)
print(final)
