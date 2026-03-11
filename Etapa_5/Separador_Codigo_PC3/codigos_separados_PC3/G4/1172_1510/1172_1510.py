#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior - 21553770
#Avaliação 04 - Exercício 03
#05/08/2016
n = int(input("Informe o número total de termos: "))
i = 1
j = 3
s = 0
k = 1
while(i <= n):
	s = s + ((i**0.5)/(4+j)) * k
	i = i+1
	j = j + 2
	k = k*(-1)
print(round(s , 9))