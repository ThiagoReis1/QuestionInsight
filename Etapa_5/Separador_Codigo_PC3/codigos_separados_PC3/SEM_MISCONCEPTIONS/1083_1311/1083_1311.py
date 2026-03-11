nota1 = float(input("digite a nota1: "))
nota2 = float(input("digite a nota2: "))
nota3 = float(input("digite a nota3: "))
media = (nota1 + nota2 + nota3) / 3
if(media>=6):	
	print(float(round(media,2)))
	print("Aprovacao")
else:
	print(float(round(media,2)))
	print("Reprovacao")