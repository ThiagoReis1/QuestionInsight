nome = input("Digite o nome do aminoacido: ")

if(nome.lower() != 'aspartato' and nome.lower() != 'cisteina' and nome.lower() != 'metionina'):
	print("Entrada: ",nome)
	print("Dado Invalido")
else:
	if(nome.lower() == 'aspartato'):
		x = ((12.011*4) + (1.00794*6) + 14.0067 + (15.9994*4))
		print(round(x, 2))
	elif(nome.lower() == 'cisteina'):
		x = ((12.011*3) + (1.00794*7) + 14.0067 + (15.9994*2) + 32.066)
		print(round(x, 2))
	elif(nome.lower() == 'metionina'):
		x = ((12.011*5) + (1.00794*11) + 14.0067 + (15.9994*2) + 32.066)
		print(round(x, 2))		