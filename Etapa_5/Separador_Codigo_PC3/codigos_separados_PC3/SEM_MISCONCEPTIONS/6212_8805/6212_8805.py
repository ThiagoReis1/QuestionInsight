numero = int(input("numero inteiro: "))

contador = 0

while(numero >= 0):
	if(26 <= numero <= 85):
		contador += 1
	numero = int(input("numero inteiro: "))
print(contador)	
	