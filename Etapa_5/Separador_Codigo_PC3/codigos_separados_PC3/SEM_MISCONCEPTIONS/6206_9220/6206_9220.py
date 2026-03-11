cont = 0
valor = int(input())

while (valor != -1):
	if (valor >= 0 and valor <= 25):
		cont += 1
		
	valor = int(input())	
		
print (cont)