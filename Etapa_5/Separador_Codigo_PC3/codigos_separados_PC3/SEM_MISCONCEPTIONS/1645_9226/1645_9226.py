from numpy import* 
#quantos saques valor >= 2000:
vetor = array(eval(input("Digite: ")))
count = 0
#zeros(len(vetor), dtype = int)

for i in range(size(vetor)):
	if (vetor[i] >= 2000):
		count = count + 1

print(count)

vetorc = zeros(count, dtype = int)
j = 0

for i in range(size(vetor)):
	if (vetor[i] >= 2000):
		vetorc[j] = i
		j = j + 1
		
print(vetorc)