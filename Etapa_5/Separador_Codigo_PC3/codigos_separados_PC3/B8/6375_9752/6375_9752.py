from numpy import*

a = input().upper().split(",")
vetor = zeros(4,dtype=int)

for i in range(size(a)):
	if a[i] == "A":
		vetor[0] = vetor[0] + 1
	elif a[i] == "B":
		vetor[1] = vetor[1] + 1
	elif a[i] == "C":
		vetor[2] = vetor[2] + 1
	elif a[i] == "D":
		vetor[3] = vetor[3] + 1
		
print(vetor)