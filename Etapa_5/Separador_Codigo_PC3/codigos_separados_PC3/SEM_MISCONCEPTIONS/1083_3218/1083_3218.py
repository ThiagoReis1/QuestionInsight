#Três provas com média 6
prova1=float(input())
prova2=float(input())
prova3=float(input())

media=(prova1+prova2+prova3)/3

if (media >= 6.0):
	mensagem="Aprovacao"
	print(round(media, 2))
	print(mensagem)
else:
	mensagem="Reprovacao"
	print(round(media, 2))
	print(mensagem)

	