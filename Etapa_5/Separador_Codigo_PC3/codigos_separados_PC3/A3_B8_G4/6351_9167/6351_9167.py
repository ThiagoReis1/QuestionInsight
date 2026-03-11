p = input("nome;   ")
i = 0
if p[-1] == 's' or p[-1] == 'S':
	print(p.upper())
elif p[-1] != 's' or p[-1] != 'S':
	print("nome invalido")