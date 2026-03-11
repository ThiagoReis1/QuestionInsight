n = int(input("Numero: "))
novo_numero1 = n // 1000
novo_numero2 = n % 1000
novo_numero3 = (novo_numero1 + novo_numero2) ** 2

if(n == novo_numero3):
	novo_numero3 = (novo_numero1 + novo_numero2) ** 2
	print("atende")
	print(n)
else:
	novo_numero3 = (novo_numero1 + novo_numero2) ** 2
	print("nao atende")
	print(n)
	
	
 
	
		