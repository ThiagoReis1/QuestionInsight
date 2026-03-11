pedido = input("qual o seu pedido: ").upper()
i = 0
preco = 0

while i <len(pedido):
	if pedido[i] == "A":
		preco = preco + 16.75
	if pedido[i] == "L":
		preco = preco + 4.60
	if pedido[i] == "P":
		preco = preco + 2.85
	i+=1
print(round(preco,2))
		