lanche = input("L ou S: ")
quantidade = int(input("Itens: "))
salgado = int(input("Salgado: "))

if lanche == "L":
	print(quantidade * 5.00 + salgado * 4.00)
else:
	print(quantidade * 3.50 + salgado * 4.00)