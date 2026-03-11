entrada = input()
contador = 0

while (entrada != 'S'):
	entrada = entrada.upper()
	if(entrada == "CARA"):
		contador+=1
	entrada = input()
print(contador)
		
		