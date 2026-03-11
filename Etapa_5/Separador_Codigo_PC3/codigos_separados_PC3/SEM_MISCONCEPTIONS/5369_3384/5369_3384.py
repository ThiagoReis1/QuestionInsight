from numpy import * 

cpf = array(eval(input("Digite o cpf: ")))

vetor_auxiliar = array([9,8,7,6,5,4,3,2,1])

total = 0
i = 0

while i < size(cpf):
	total = total + cpf[i] * vetor_auxiliar[i]
	i = i + 1
	
print(total % 11)