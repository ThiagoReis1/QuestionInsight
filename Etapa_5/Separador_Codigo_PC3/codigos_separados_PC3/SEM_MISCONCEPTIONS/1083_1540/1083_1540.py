#UNIVERSIDADE FEDERAL DO AMAZONAS
#Thiago Tuma Camilo 21600549

nota1 = float(input("Qual o valor da nota 1?"))
nota2 = float(input("Qual o valor da nota 2?"))
nota3 = float(input("Qual o valor da nota 3?"))

media_notas = (nota1 + nota2 + nota3) / 3

if (media_notas >= 6):
	print(round(media_notas, 2))
	print("Aprovacao")
else:
	print("")