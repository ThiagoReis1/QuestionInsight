nota1=float(input("qual a nota 1 ?"))
nota2=float(input("qual a nota 2 ?"))
nota3=float(input("qual a nota 3 ?"))
nota4=float(input("qual a nota 4 ?"))
nota5=float(input("qual a nota 5 ?"))
media=(nota1+nota2+nota3+nota4+nota5)/5
if(media >= 5):
	print(round(media, 1))
	print("Aprovado")
else:
	print(round(media, 1))
	print("Reprovado")