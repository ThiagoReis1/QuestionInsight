item = input("digite o item: ")
q_item = int(input("digite a quantidade: ")) 
q_refrigerantes = int(input("digite a quantidade: "))

if("L"==item):
	preco = 6.00 * q_item + 3.00 * q_refrigerantes
	print(preco)
else:
	preco = 13.50 * q_item + 3.00 * q_refrigerantes
	print(preco)