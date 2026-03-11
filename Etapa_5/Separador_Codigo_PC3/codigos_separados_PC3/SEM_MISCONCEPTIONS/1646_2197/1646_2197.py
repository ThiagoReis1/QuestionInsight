from numpy import*
vetor = array(eval(input("Digite valor do vetor: ")))
saque = 0
r = 0

for i in range(size(vetor)):
	if vetor[i] <= 50:
		saque = saque + (vetor[i] <= 50)
print(saque)

for i in range(size(vetor)):
	if vetor[i] <= 50:
		r = array(
print(r)