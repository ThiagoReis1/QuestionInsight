
letra = input('Digite uma palavra; ').upper()

cont = 0
i = 0

while i < len(letra):
	if letra[i] == 'A' or letra[i] == 'E' or letra[i] == 'I' or letra[i] == 'O' or letra[i] == 'U':
		cont = cont + 45.12
	else:
		cont = cont + 50.18
	i = i + 1
	
print(cont)