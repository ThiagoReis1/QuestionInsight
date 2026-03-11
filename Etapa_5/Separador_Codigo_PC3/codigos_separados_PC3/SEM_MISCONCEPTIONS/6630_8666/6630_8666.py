
entrada = input("Digite uma string: ").upper()

i = 0

while i < len(entrada):
	if entrada[i] == 'L':
		print(i)
	i += 1
	
if 'L' not in entrada:
	print('nao achei')