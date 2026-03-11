nota1=float(input("digite a 1 nota:"))
nota2=float(input("digite a 2 nota:"))
nota3=float(input("digite a 3 nota:"))
nota4=float(input("digite a nota 4:"))

media = (nota1+nota2+nota3+nota4)/4

if (media>=5):
	print(round(media,2))
	mensagem="Aprovacao"
else:
	print(round(media,2))
	mensagem="Reprovacao"
print(mensagem)