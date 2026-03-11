from numpy import*
vetor = array(eval(input("Informe o vetor: ")))
i=0
qtd=0
while(i < size(vetor)):
	if(vetor[i] < 307):
		qtd = qtd + 1
	i = i + 1
print("307")
print(qtd)