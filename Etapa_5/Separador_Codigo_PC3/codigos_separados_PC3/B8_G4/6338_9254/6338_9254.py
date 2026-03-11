from numpy import*
vetor = array(eval(input("insira o vetor: ")))
n = int(input("insira um numero inteiro: "))

i = 0  #contadora para indice do vetor
k = 0  #ocorrencias
while i < size(vetor):
	if vetor[i] == n:
		print(i)
	elif vetor[i] > n:
		k = k + 1
	i = i + 1

print(k)