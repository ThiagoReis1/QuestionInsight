numero=int(input("identifique o numero da sorte "))
quant=0
while(numero!=-1):
	if numero >= 51 and numero <= 75:
		quant += 1
	numero=int(input("identifique o numero da sorte "))
print(quant)