from numpy import*

vet = array(eval(input("Digite o vetor: ")))
num = int(input("Digite um numero inteiro: "))


aux = 0
for i in range(size(vet)):
	if vet[i] == num:
		print(i)

total = 0
for i in range(size(vet)):
	if vet[i] < num:
		total += 1
print(total)