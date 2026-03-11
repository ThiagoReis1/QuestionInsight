from numpy import* 

vetor = array(eval(input("Informe os valores: ")))

i = 0 
soma = 0
while i < size(vetor):
	if vetor[i] == 1:
		soma = soma + 80
	elif vetor[i] == 2:
		soma = soma + 40
	elif vetor[i] == 3:
		soma = soma + 20
	elif vetor[i] == 4:
		soma = soma + 10
	i =  i + 1
print(soma)
		
		