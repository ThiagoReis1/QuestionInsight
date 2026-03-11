numero = int(input("digite numero: "))
valores_do_intervalo = 0

while (numero != -1):
	
	if (numero >= 100 and numero <= 199):
		valores_do_intervalo = valores_do_intervalo + 1
		
	numero = int(input("digite numero: "))
		
print(valores_do_intervalo)