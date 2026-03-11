n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())
media=(n1+n2+n3+n4+n5)/5
if(media>=5):
	print(round(media, 1))
	print("Aprovado")
else:
	print(round(media, 1))
	print("Reprovado")