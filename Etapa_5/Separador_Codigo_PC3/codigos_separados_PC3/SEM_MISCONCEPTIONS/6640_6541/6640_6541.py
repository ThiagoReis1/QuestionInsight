# faça seu código aqui!
palavra = input()

i = 0
contador = 0

while i < len(palavra):
	if palavra[i].upper() == 'N':
		contador += 1
		print(i)
		
	i += 1
	
if contador == 0:
	print("nao achei")