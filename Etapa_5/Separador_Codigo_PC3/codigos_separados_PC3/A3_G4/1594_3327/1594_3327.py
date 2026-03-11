from numpy import*
vetor = array(eval(input("Digite um numero: ")))
i = 0
cont = 0
soma = 0
while(i < size(vetor)):
	soma = soma + vetor[i] * (i+1)
	i = i + 1
print(soma)