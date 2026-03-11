quantidade = input().upper()
estudante = 0

while(quantidade != 'X'):
	if quantidade == 'FT':
		estudante += 1
	quantidade = input().upper()
	
print(estudante)
		