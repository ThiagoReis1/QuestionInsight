from numpy import*
y=input("Coloque os nomes:")
vetor=y.split(",")
result=zeros(5, dtype = int)
for i in range(size(vetor)):
	if vetor[i] == 'B':
		result[0] = result[0] + 1
	elif vetor[i] == 'PA':
		result[1] = result[1] + 1
	elif vetor[i] == 'PR':
		result[2] = result[2] + 1
	elif vetor[i] == 'A':
		result[3] = result[3] + 1
	elif vetor[i] == 'I':
		result[4] = result[4] + 1
print(max(result))
print(result)
	