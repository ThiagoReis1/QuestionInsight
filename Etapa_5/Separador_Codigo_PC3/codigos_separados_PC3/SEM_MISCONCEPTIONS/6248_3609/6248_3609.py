letra = input().upper()
cont = 0
while (letra != 'X'):
	if(letra == 'A'):
		cont +=1
	letra = input().upper()
print(cont)