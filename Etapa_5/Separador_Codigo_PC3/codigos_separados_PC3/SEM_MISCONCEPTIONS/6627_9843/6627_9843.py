# faça seu código aqui!
from numpy import*

palavra = input("Digite a string: ").upper()

cont = 0
for i in range(len(palavra)):
	if palavra[i] == "D":
		cont = cont + 1

print(cont)
