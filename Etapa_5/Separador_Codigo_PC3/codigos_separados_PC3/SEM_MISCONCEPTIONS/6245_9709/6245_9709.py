resposta = input("responda S I N ou X: ").upper()
clientes_satisfeitos = 0

while resposta!= "X":
	if resposta == "S":
		clientes_satisfeitos += 1
		
	resposta = input("responda S I N ou X: ").upper()
print(clientes_satisfeitos)