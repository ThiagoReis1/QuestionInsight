nota1 = float(input( "digite a nota" ))
nota2 = float(input( "digite a nota" ))
nota3 = float(input( "digite a nota" ))
nota4 = float(input( "digite a nota" ))
nota5 = float(input( "digite a nota" ))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print(round(media,2))

if  (media>= 6) :
	print ("Aprovado")
	
else:
	print("Reprovado")
	
