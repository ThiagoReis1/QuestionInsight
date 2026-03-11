# Entrada

lado = input("Lado da moeda:")

cara = 0
outros = 0

# Repeticao

while (lado.upper() != "S"):
	if (lado.upper() == "CARA"):
		cara = cara + 1
	else:
		outros = outros + 1
	lado = input("Lado da moeda:")

jogadas = cara + outros 
resultado = (cara / jogadas) * 100

print(jogadas)
print(round(resultado,2))