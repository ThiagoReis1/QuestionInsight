nota1= float(input("insira a nota 1"))
nota2= float(input("insira a nota 2"))
nota3= float(input("insira a nota 3"))
nota4= float(input("insira a nota 4"))
media= round((nota1+nota2+nota3+nota4)/4,2)
if media>=5:
	print(media,"Aprovacao")
else:
	print(media,"Reprovacao")