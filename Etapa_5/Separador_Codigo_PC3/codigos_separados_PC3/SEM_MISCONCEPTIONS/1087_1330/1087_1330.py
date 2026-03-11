nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
if ((nota1+nota2+nota3+nota4)/4>=7):
	notafinal = (nota1+nota2+nota3+nota4)/4
	print (round(notafinal,2))
	print ("Aprovado")
else:
	notafinal = (nota1+nota2+nota3+nota4)/4
	print (round(notafinal,2))
	print ("Reprovado")