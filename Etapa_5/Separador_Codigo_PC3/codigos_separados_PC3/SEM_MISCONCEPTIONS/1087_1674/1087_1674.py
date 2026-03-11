nota_1 = float(input("Qual a primeira nota?"))
nota_2 = float(input("Qual a segunda nota?"))
nota_3 = float(input("Qual a terceira nota?"))
nota_4 = float(input("Qual a quarta nota?"))
media = (nota_1 + nota_2 + nota_3 + nota_4 ) / 4
print(round(media ,2))
if(media >= 7):
	print("Aprovado")
else:
	print("Reprovado")