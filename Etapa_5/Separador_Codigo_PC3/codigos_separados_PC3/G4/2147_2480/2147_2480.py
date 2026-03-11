from numpy import*

cpf = input("CPF: ").split()
i = 0
cpf2 = ""

while(i <= len(cpf)):
	if(i % 2 != 0):
		cpf2 = cpf2 + cpf[i]
	i = i + 1
	print (cpf2)