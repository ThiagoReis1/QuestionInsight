nota1=float(input("digite nota1"))
nota2=float(input("digite nota2"))
nota3=float(input("digite nota3"))
nota4=float(input("digite nota4"))
nota5=float(input("digite nota5"))
media=(nota1+nota2+nota3+nota4+nota5)/5
if(media>=5):
	mensagem="Aprovado"
	print(round(media,1))
	print(mensagem)
else:
	mensagem="Reprovado"
	print(round(media,1))
	print(mensagem)