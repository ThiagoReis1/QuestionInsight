nota1=float(input())
nota2=float(input())
nota3=float(input())
media=(nota1+nota2+nota3)/3
print(round(media,1))
if media>=5.0:
	mensagem="Aprovado"
	print(mensagem)

else:
	mensagem="Reprovado"
	print(mensagem)
