#Lucas Nascimento Estevam da Silva		21602757
#Trabalho Pratico 05
#Exercicio 03

from numpy import*

t = array(eval(input("Tempos: ")))
m = array(eval(input("Modos: ")))
i = 0
v = 0

while(i < size(t)):
	if(m[i] == "QUENTE"):
		v = v + (0.005 * 90 *t[i])
	elif(m[i] == "MORNO"):
		v = v + (0.005 * 45 * t[i])
	elif(m[i] == "FRIO"):
		v = v + 0
	i = i + 1
print(round(v,2))