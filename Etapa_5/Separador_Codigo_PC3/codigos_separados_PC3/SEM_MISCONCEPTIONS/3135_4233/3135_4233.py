from numpy import*

vetor = array(eval(input("Digite um numero: ")))

tamanho = size(vetor)
i = 0
n = 0

while(i<tamanho):
	n = n + 1
	i = i + 1

m = arange(n)
n = n + 1


while(i<size(tamanho)):
	n = (n + (m[i]**2) + (1/2**m))
	m = m + 1
	
print(vetor)
	
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											


	
