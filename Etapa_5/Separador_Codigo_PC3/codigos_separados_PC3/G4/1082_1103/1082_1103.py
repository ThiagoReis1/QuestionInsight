from math import*
n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())
media=(n1+n2+n3+n4+n5)/5
print(round(media,1))
if(media>=5.0):
	mensagem="Aprovado"
	
else:
	mensagem="Reprovado"
print(mensagem)	