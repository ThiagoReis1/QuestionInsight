opcao = input ("aprovado ? (aprovado/reprovado)")
prova1 = float(input("digite nota 1:"))
prova2 = float(input("digite nota 2:"))
prova3 = float(input("digite nota 3:"))
prova4 = float(input("digite nota 4:"))
nota_total = (prova1 + prova2 + prova3 + prova4) / 4
if(opcao == aprovado)
	nota_total >= 6
	print(nota_total)
if(opcao == reprovado)
	nota_total < 6
	print(nota_total , 2)