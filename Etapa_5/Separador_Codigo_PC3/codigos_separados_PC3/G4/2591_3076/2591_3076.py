from numpy import*
#vetor ocorrencia
vet = array(eval(input("")))
#variaveis, indice exceto o primeiro
s = 0
oc = -vet[0]
#condição
for i in range(size(vet)):
	if(vet[i]<=oc and vet[i]!=vet[0]):
		print(i)
		s = s + 1

print(s)