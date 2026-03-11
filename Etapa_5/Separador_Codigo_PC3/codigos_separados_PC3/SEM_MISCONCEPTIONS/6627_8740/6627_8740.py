# faça seu código aqui!
from numpy import*

palavra = input("").upper()

contador_c=0
i = 0
tamanho = len(palavra)
while i < tamanho:
	if palavra[i] == "D":
		contador_c += 1 
	i +=1
print (contador_c)