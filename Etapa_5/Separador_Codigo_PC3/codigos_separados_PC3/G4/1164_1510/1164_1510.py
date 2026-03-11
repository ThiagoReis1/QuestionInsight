#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior - 21553770
#Avaliação 04 - Exercício 01
#05/08/2016
n = int(input("Informe o número total de termos: "))
i =1 
j = 1 #variavel do denominador
k = 1 #auxiliar de sinal da operação
s = 0
while(i <= n):
	s = s + ((i**2)/(4+j)) * k
	i = i+1
	j = j + 2
	k = k*(-1)
print(round(s, 8))