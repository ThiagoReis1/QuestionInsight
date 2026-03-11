#universidade federal do amazonas
# Laura Cristina Soares Santos - 21650872

nota_1=float(input("insira 1 nota: "))
nota_2=float(input("insira 2 nota: "))
nota_3=float(input("insira 3 nota: "))
nota_4=float(input("insira 4 nota: "))
nota_5=float(input("insira 5 nota: "))

media = round(((nota_1+nota_2+nota_3+nota_4+nota_5)/5), 1)

print(media)

if (media >= 5) :
	print("Aprovado")
else :
	print("Reprovado")
	