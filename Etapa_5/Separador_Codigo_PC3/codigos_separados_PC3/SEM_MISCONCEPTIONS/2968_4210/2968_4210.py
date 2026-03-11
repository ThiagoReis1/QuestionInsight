pedido = input("Lanche ou salgado? (L/S)")
quantidade = int(input("Qual a quantidade?"))
refri = int(input("Quantos Refrigerantes?"))
L = 5.00
S = 3.50
R = 4.00
preco1 = float((L*quantidade)+(R*refri))
preco2 = float((S*quantidade)+(R*refri))

if(pedido.upper()=='L'):
	print(round(preco1,2))
else:
	print(round(preco2,2))