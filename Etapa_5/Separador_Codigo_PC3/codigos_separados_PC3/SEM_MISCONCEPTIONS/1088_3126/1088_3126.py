nota1 = float(input("prova um:"))
nota2 = float(input("prova dois:"))
nota3 = float(input("prova tres:"))
nota4 = float(input("prova quatro:"))
nota5 = float(input("prova cinco:"))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
if (media >= 7):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao por nota")