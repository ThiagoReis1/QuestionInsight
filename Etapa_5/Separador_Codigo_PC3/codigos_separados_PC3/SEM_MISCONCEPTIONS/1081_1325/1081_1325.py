nota1 = float (input ("nota 1: "))
nota2 = float (input ("nota 2: "))
nota3 = float (input ("nota 3: "))
nota4 = float (input ("nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media>=5:
	print (round (media,2))
	print ("Aprovacao")
else:
	print (round (media,2))
	print ("Reprovacao")