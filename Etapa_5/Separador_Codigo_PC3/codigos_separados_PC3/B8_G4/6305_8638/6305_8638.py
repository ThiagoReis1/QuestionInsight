produtos = input(":").upper()
i = 0
cont = 0
c1 = 0
c2 = 0
c = 0
while i < len(produtos):
	if produtos[i] == 'H':
		cont = cont + 3.85
		c = c + 1
	elif produtos[i] == 'L':
		cont = cont + 2.95
		c1 = c1 + 1
	elif produtos[i] == 'E':
		cont = cont + 7.90
		c2 = c2 + 1
	i = i + 1
print(round(cont, 2)), print(c), print(c1), print(c2)




