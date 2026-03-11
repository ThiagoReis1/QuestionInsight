# faça seu código aqui!
palavra = input('insira a palavra: ').upper()

i = 0
P = 0
letra = 0 

while i < len(palavra):
	if palavra[i] == 'P':
		print(i)
	i += 1

if 'P' not in palavra:
	print('nao achei')
	
	
	