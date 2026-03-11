nota_1=float(input("Nota 1:"))
nota_2=float(input("Nota 2:"))
nota_3=float(input("Nota 3:"))
nota_4=float(input("Nota 4:"))
nota_5=float(input("Nota 5:"))
media= (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

if(media >= 6.00):
	print(round(media,2))
	print("Aprovado")
else:
	print(round(media,2))
	print("Reprovado")
		