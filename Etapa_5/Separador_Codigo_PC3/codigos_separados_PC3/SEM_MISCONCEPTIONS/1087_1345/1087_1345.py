nota1=float(input("Nota1:"))
nota2=float(input("Nota2:"))
nota3=float(input("Nota3:"))
nota4=float(input("Nota4:"))

media=round((nota1+nota2+nota3+nota4)/4,2)

if (media>=7):
	print(media,"Aprovado")	
else:
	print(media,"Reprovado")