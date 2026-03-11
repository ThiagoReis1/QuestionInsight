#Lucas Nascimento Estevam da Silva		21602757
#Trabalho Pratico 05
#Exercicio 01

from numpy import*

v = array(eval(input("Valores: ")))
d = 15 / 100
i = 0

while(i < size(v)):
	if(v[i] >= 80.0):
		v[i] = v[i] - (d * v[i])
	i = i + 1
	
print(sum(v))