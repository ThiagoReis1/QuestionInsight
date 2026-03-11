x = str(input("Digite o pedido [C] ou [E]: "))
if x == "C":
	qtd = int(input("Digite a quantidade de coxinhas: "))
	sucos = int(input("Digite a quantidade de sucos: "))
	total = (qtd*2.00) + (sucos*6.00)
	print(total)
if x == "E":
	qtd = int(input("Digite a quantidade de esfirras: "))
	sucos = int(input("Digite a quantidade de sucos: "))
	total = (qtd*4.50) + (sucos*6.00)
	print(total)