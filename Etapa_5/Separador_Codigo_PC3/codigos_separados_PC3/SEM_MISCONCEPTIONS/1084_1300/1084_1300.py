prova1 = float(input("digite a primeira nota:"))
prova2 = float(input("digite a segunda nota "))
prova3 = float(input("digite a terceira nota "))
prova4 = float(input("digite a quarta nota "))

media = (prova1 + prova2 + prova3 + prova4) / 4

print(round(media,1))



if(media < 6):
	print("Reprovado")
else:
	print("Aprovado")
	

	

