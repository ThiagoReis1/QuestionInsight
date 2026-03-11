mensagem = [int() for x in input().split()]
for i in range(len(mensagem)):
	if mensagem[i] == 0:
		mensagem[i] = (9**2)
	else:
		mensagem[i]=(mensagem[i]-1)**2
print(mensagem)