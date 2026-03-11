from numpy import*
vetor = array(eval(input("digite vetor: ")))
x = 0
impar = 0
for x in range (size(vetor)):
		if (vetor[x] % 2 == 1):
			impar = impar + 1
print(impar)
vetor1 = arange(impar)
i = 0
for x in range (size(vetor)):
	if (vetor[x] %2 == 1):
		vetor1[i] = x
		i = i + 1
print(vetor1)
