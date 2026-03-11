tapioca_salgado = input("T ou S: ")
quantidade_itens = int(input("itens: "))
quantidade_acai = int(input("Acai: "))

if tapioca_salgado == "T":
	print(quantidade_itens * 5.50 + quantidade_acai * 10.00)
else:
	print(quantidade_itens * 4.00 + quantidade_acai * 10.00)
	

