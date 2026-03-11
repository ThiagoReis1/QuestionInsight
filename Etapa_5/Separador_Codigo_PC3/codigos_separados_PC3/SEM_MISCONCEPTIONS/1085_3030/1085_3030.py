nota1 = float(input("Qual sua primeira nota?"))
nota2 = float(input("Qual sua segunda nota?"))
nota3 = float(input("qual sua terceira nota?"))
nota4 = float(input("qual sua terceira nota?"))
nota5 = float(input("qual sua quinta nota?"))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print(round(media,2))
if(media >= 6):
	print("Aprovacao")
else:
	print("Reprovacao")
