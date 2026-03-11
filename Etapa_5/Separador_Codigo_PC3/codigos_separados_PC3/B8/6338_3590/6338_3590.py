vetor = eval(input())
num = int(input())

maiores = 0
i = 0
while(i < 8):
	if(vetor[i] == num):
		print(i)
	elif(vetor[i] > num):
		maiores += 1
	i += 1
print(maiores)