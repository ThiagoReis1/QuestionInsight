dado = int(input("Digite o valor do dado: "))
i = 1
while(i > 0):
	if(dado == 6):
		print(i)
		i = -1
	else:
		dado = int(input("Digite o valor do dado: "))
		i = i+1
		