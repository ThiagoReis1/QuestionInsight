# faça seu código aqui!
from numpy import*

frase = input('').upper()
i = 0 

while i < len(frase):
	if frase[i] == 'N':
		print(i)
	i = i + 1
if 'N' not in frase:
	print('nao achei')