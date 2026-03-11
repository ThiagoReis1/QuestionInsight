nota1 = float(input("insira uma nota: "))
nota2 = float(input("insira uma nota: "))
nota3 = float(input("insira uma nota: "))
media = round(((nota1 + nota2 + nota3)/3), 2)
if(media >=6):
	print(media)
	print("Aprovacao")
else:
	print(media)
	print("Reprovacao")
	
	