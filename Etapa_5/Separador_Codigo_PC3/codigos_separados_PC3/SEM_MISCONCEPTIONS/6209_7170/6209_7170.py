numero = int(input("Numero: "))

erro = 0

while numero >= 0:
	while numero >= 76 and numero <= 100:
		numero = int(input("Numero: "))
		erro += 1
		
	if numero << 76:
		numero = int(input("Numero: "))

print(erro)