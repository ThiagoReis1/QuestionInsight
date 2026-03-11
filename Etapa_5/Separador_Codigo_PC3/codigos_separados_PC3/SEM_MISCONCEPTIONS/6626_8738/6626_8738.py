# faça seu código aqui!
frase = input("coloque a frase: ")
frase = frase.upper()

contador_c = 0
i = 0
tamanho = len(frase)
while i < tamanho:
	if frase[i] == "C":
		contador_c += 1
	i += 1
print(contador_c)