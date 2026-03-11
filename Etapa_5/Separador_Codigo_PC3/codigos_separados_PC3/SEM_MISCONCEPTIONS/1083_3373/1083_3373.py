a=float(input())
b=float(input())
c=float(input())
media=(a+b+c)/3
if (media >= 6.0):
	mensagem="Aprovacao"
else:
	  mensagem="Reprovacao"
print(round(media,2))
print(mensagem)