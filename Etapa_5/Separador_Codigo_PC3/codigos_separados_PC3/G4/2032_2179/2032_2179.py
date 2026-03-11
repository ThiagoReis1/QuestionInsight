dado = int(input("Dado lançado: "))
i = 0

while(dado!= -1):
	if(dado == 5):
		i = i + 1
	
	dado = int(input("Dado lançado: "))
	
print(i)