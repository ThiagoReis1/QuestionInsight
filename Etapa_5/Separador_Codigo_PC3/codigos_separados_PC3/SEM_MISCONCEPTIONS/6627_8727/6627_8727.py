# faça seu código aqui!
letra = input("coloque a frase:")
letra = letra.upper()

contador_d = 0
i = 0
tamanho = len(letra)

while i < tamanho:
	if letra[i] == "D":
	   contador_d += 1
	i+= 1
print(contador_d)