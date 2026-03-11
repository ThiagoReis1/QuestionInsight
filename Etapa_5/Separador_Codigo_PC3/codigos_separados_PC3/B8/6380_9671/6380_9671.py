from numpy import *

escolha = input("insira as categorias escolhidas: ").upper().split(',')

v = zeros(4, dtype=int)

for i in range(size(escolha)):
	if escolha[i] == 'E':
		v[0] = v[0] + 1
	elif escolha[i] == 'V':
		v[1] = v[1] + 1
	elif escolha[i] == 'A':
		v[2] = v[2] + 1
	elif escolha[i] == 'D':
		v[3] = v[3] + 1
		
print(v)