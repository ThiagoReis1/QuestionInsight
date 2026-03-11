from numpy import *
vetor = array(eval(input()))
vetor2 = array(eval(input()))
i = 0
b = 0.97
c = 2.95
f = 1.27
o = 1.04
t = 0.2
novo = 0

while(i<size(vetor)):
	if(vetor[i]=="BANANA"):
		novo = novo + b * vetor2[i]
	elif(vetor[i]=="BIFE"):
		novo = novo + c * vetor2[i]
	elif(vetor[i]=="FEIJOADA"):
		novo = novo + f * vetor2[i]
	elif(vetor[i]=="OMELETE"):
		novo = novo + o * vetor2[i]
	elif(vetor[i]=="TOMATE"):
		novo = novo + t * vetor2[i]
	i = i + 1
print(round(novo,2))
		

