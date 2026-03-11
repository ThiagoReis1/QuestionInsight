# faça seu código aqui!
frase = input("digite a frase aqui: ")
frase = frase.upper()
i = 0
tamanho = len(frase)

while i < tamanho:
	if frase[i] == "M":
		print(i)
	i = i + 1
if "M" not in frase:
	print("nao achei")

	
