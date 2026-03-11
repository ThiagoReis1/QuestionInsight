nota_1= float(input())
nota_2= float(input())
nota_3= float(input())
nota_4= float(input())
nota_5= float(input())

media= (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

if (media >= 7):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao por nota")
