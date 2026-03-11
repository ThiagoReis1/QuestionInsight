from numpy import * 

vetort = array(eval(input("Digite o tempo de chegada dos corredores: ")))
#p / percorrer o vetor
st = size(vetort)
i = 0 

while (i < st):
	if(vetort[i] == max(vetort)):
		print(i)
	i = i + 1
