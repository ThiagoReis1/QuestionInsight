from numpy import*

cpf = array(eval(input("Digite: ")))
vetor = [1,2,3,4,5,6,7,8,9]
i = 0
while i < size(cpf):
	cpf[i] = cpf[i]*vetor[i]
	i = i + 1
Total_Soma = sum(cpf)
Resto = Total_Soma % 11

print(Resto)	
