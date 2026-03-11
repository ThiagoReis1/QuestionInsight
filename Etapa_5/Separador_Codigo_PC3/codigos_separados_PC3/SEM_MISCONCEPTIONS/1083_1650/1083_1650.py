nota1 = float(input("Qual o valor da nota 1?"))
nota2 = float(input("Qual o valor da nota 2?"))
nota3 = float(input("Qual o valor da nota 3?"))

media = (nota1+nota2+nota3) / 3.0

if (media >= 6.0):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao")
	