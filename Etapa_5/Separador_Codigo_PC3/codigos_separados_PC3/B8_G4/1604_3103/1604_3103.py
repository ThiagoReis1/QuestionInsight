from numpy import*
vp = array(eval(input("Qual o vetor de numeros dos aneis?: ")))
soma = 0
i = 0
while(i < size(vp)):
	if(vp[i] == 1):
		soma = soma + 80
	elif(vp[i] == 2):
		soma = soma + 40
	elif(vp[i] == 3):
		soma = soma + 20
	elif(vp[i] == 4):
		soma = soma + 10	
	i = i + 1
print(soma)	