prova1 = float(input("valor da 1 prova"))
prova2 = float(input("valor da 2 prova"))
prova3 = float(input("valor da 3 prova"))
prova4 = float(input("valor da 4 prova"))
media = (prova1 + prova2 + prova3 + prova4) / 4
print(round(media, 1))

if(media >=6):
	print("Aprovado")
else:
	print("Reprovado")