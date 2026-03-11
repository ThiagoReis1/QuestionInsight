numero = int(input("Digite o numero: "))
contagem = 0

while numero != -1:
	
	if numero >= 51 and numero <= 75:
		contagem = contagem + 1
	numero = int(input("Digite o numero: "))	
	
print(contagem)