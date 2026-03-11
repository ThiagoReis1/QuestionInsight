# faça seu código aqui!
frase= input()
frase= frase.upper()
i=0
while i<len(frase):
	if frase[i]=='L':
		print(i)
	i+=1
if 'L' not in frase:
	print('nao achei')

