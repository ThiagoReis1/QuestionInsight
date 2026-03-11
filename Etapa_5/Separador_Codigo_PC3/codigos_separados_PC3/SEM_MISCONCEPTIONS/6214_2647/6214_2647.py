contador = 0
entrada = int(input())
while(entrada != -1):
	if((entrada >= 45) and (entrada <= 150)):
		contador+=1
	entrada =int(input())
print(contador)