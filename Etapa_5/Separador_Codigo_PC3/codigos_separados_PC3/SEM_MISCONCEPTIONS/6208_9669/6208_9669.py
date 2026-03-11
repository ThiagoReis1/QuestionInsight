numero = int(input("Entre com o numero da sorte: "))

contador = 0

while numero != -1:
	if numero >= 51 and numero <= 75:
		contador = contador + 1 
	numero = int(input("Entre com o numero da sorte: "))
	
print(contador)