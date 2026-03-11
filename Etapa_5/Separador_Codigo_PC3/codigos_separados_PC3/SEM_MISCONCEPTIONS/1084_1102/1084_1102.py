from math import*
nota1=float(input(""))
nota2=float(input(""))
nota3=float(input(""))
nota4=float(input(""))
media=((nota1+nota2+nota3+nota4)/4)
if (((nota1+nota2+nota3+nota4)/4)>=6):
	msg="Aprovado"
	print(round(media,1))
	print(msg)
else:
	msg="Reprovado"
	print(round(media,1))
	print(msg)