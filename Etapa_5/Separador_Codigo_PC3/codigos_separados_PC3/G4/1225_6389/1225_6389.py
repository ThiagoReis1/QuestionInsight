from numpy import * 

vetor = array(eval(input("Digite numeros reais: ")))
i = 0
m = sum(vetor) / size(vetor)
x = 0
for i in range(size(vetor)):
	x = x + (vetor[i] - m)**2
	
a = (x / (size(vetor) - 1)) ** (1/2)

print(round(a, 3))