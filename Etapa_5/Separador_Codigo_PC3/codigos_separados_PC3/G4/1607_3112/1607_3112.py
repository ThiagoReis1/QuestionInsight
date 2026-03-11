from numpy import*
#Entradas
vetor = array(eval(input("Vetor contendo os andares que o elevador parou: ")))

#variavel acmuladora
i = 0
ii = i + 1
d = 0

while(i < size(vetor)):
	cal = (vetor[ii] - vetor[i]) * 3
	d = d + cal
	i = i +  1
print(d)
	
	

