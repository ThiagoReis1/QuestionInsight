numero = int(input("Numero saudavel: "))
contador = 0 

while numero != -1:
	if numero >= 26 and numero <= 85:
		contador += 1
		numero = int(input("Numero saudavel: "))
	else:
		numero = int(input("Numero saudavel: "))
	
print(contador)
	