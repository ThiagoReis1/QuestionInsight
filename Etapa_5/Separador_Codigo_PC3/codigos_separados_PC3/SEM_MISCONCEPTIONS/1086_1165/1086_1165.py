prova_A = float(input("Insira uma nota A: "))
prova_B = float(input("Insira uma nota B: "))
prova_C = float(input("Insira uma nota C: "))
media = (prova_A + prova_B + prova_C) / 3
if (media >= 7):
	print(round(media, 1))
	print("Aprovacao")
else:
	print(round(media, 1))
	print("Reprovacao")
				  
	