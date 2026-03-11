# faça seu código aqui!
from numpy import*

nome = input().upper()

i = 0
if 'L' not in nome:
	print('nao achei')
while i < len(nome):
	if nome[i] == 'L':
		print(i)
	i += 1