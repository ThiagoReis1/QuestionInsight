# faça seu código aqui!
from numpy import*

f = input("Insira a palavra: ").upper()

contador_c = 0
tamanho = len(f)
i = 0

while i < tamanho:
	if f[i] == "C":
		contador_c += 1
	i +=1
print(contador_c)