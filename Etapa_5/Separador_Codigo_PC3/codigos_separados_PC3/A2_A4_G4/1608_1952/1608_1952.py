#Lucas Nascimento Estevam da Silva		21602757
#Prova Final
#Exercicio 01

from numpy import*

vet = array(eval(input("Numeros :")))
max = 75
s = 0
for i in range(size(vet)):
	s = s + vet[i]
if(s > max):
	s = 75
else:
	s = s
print(s)