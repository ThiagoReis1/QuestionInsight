#Lucas Nascimento EStevam da Silva		Matricula: 21602757
#Trabalho Pratico 04
#Exercicio 2

from math import*

x = int(input("Numero: "))
k = int(input("Numero de series: "))
s = 1
i = 1
a = 1

if(k > 0):
	
	while(i < k):
		s = s + (x ** (2 * a)) / factorial(2 * a)
		a = a + 1
		i = i + 1
		
print(round(s,8))