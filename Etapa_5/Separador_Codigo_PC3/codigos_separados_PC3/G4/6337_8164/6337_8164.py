from numpy import*
vet = array(eval(input("digite o vetor: ")))
n = int(input("digite um numero: "))
i = 0
ac = 0

while i<size(vet):	
	if vet[i] == n:
		print(i)
	if vet[i] < n:
		ac = ac + 1
	i = i + 1 
print(ac)