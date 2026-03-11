# faça seu código aqui!

nome = input("Informe uma palavra: ").upper()

i = 0

if "N" not in nome:
	print("nao achei")
	
else:
	while i < len(nome):
	
		if nome[i] == "N":
			print(i)
		
		i = i + 1
	
	