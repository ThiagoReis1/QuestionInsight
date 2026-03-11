entrada = input()
entrada1 = entrada.replace("[", "").replace("]", "").split(",")

vetor = []

n = int(input())

for i in entrada1:
	vetor.append(int(i))

j = 0
c = 0
while j < len(vetor):
	if vetor[j] == n:
		print(j)
		
	if vetor[j] < n:
		c = c+1
	j = j+1
	
print(c)