palavra = input("palavra: ").upper()
contador = 0
indice = 0
while indice < len(palavra):
	if palavra[indice] == 'P':
		print(indice)
	indice = indice+1
if 'P' not in palavra:
   print("nao achei ")