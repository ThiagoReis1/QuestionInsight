nota_1 = float(input("Digite nota 1: "))
nota_2 = float(input("Digite nota 2: "))
nota_3 = float(input("Digite nota 3: "))
media = (nota_1 + nota_2 + nota_3)/3
print (round(media,1))
if(media >= 5):
	print ("Aprovado")
else:
	print ("Reprovado")