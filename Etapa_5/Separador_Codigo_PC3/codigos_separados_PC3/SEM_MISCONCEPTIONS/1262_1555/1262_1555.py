from numpy import*

vetor = array(eval(input("Informe vetor: ")))


n = size(vetor)
media = sum(vetor)/n
soma = 1

for i in range(n):
	 soma = soma * (abs(vetor[i] - media))
p = soma**(1/n)
print(round(p, 6))