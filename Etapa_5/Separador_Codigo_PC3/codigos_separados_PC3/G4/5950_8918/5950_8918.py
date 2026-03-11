a = (input("Digite 'T' ou 'P': "))
f = int(input("Digite quantidade de fatias da torta: "))
c = int(input("Digite quantidade de cappuccinos: "))

if (a == 'T'):
	valor = f * 6 + c * 4.50
else:
	valor = f * 5 + c * 4.50
print(round(valor,2))


	
	 