from numpy import*
e = array(eval(input("Informe o vetor entrada: \n")))
s = array(eval(input("Informe o vetor saida: \n")))
i = 0
aux = 0
soma = 0
soma2 = 0

while(i<size(e)):
	aux = aux + e[i]
	if(aux<=75):
		soma = soma - s[i] + aux
	elif(soma>75):
		aux = 75 - s[i]
	i = i + 1
print(soma)