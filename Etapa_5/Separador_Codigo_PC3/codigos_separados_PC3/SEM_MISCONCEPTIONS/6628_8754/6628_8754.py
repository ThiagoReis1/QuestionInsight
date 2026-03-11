# faça seu código aqui!
frase = input("Coloque a frase: ")
frase = frase.upper()

contador_e = 0
i = 0
tamanho = len(frase)
while i < tamanho:
	if frase[i] == "E":
		contador_e += 1
	i += 1
print(contador_e)