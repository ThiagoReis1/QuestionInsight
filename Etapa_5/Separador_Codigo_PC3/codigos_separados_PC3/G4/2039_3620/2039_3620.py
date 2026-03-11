seq = 0
cont = 0
while seq != 'S':
	seq = input('Insira a sequencia: ').upper()
	if seq == 'A':
		cont = cont + 1
print(cont)