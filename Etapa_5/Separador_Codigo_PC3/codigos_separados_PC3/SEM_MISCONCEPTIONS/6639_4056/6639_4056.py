# faça seu código aqui!
frase = input("coloque a frse: ")
frase = frase.upper()

contador_e = 0
i = 0
tamanho = len(frase)

while i < tamanho:
	if frase [i] == "M":
		contador_e += 1
		print(i)
	i += 1
if contador_e == 0:
	print("nao achei")