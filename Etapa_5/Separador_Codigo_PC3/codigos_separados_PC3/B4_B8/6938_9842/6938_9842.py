valor = float(input("valor do plano: "))
tipo = str(input("informe o codigo: "))

if(tipo.upper() == 'D'):
	total = valor - (valor) * (11/(100))
	print(round(total, 2))
else:
	if(tipo.upper() == 'P'):
		total = valor - (valor) * (11/(100))
		print(round(total, 2))
	else:
		if(tipo.upper() == 'C'): 
			n = int(input("quantas vezes: "))
			if(n == 1):
					print(round(valor, 2))
			if(n == 2):
					total = valor + (valor) * (6/(100))
					print(round(total, 2))
