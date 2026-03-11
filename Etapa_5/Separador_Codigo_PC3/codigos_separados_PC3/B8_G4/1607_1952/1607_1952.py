#Lucas Nascimento Estevam da Silva		21602757
#Trabalho Pratico 05
#Exercicio 02

from numpy import*

a = array(eval(input("Andares: ")))
i = 0
v = 0

while(i < size(a)):
	if(i < size(a) - 1):
		if(a[i + 1] - a[i] < 0):
			v = v + (-1) * ((a[i + 1] - a[i]) * 3)
		elif(a[i + 1] - a[i] > 0):
			v = v + ((a[i+1] - a[i]) * 3)
	elif(i > size(a) - 1):
		if(a[i] - a[i - 1] < 0):
			v = v + (-1) * ((a[i] - a[i - 1]) * 3)
		elif(a[i] - a[i - 1] > 0):
			v = v + ((a[i] - a[i - 1]) * 3)
	i = i + 1
	
print(v)