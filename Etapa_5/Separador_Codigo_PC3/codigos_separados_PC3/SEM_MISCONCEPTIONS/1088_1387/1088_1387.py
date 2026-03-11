nota1 = float(input("insira nota 1"))
nota2 = float(input("insira nota 2"))
nota3 = float(input("insira nota 3"))
nota4 = float(input("insira nota 4"))
nota5 = float(input("insira nota 5"))
print(nota1, nota2, nota3, nota4, nota5)
media = (round(nota1 + nota2 + nota3 + nota4 + nota5) /5 , 2)
print(media)
if( media  >= 7 ) :
	print("Aprovacao")
else : 
	print("Reprovacao") 
	