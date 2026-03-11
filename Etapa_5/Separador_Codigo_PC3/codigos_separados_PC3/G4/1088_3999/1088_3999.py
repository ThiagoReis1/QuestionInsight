n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())
media=(n1+n2+n3+n4+n5)/5
if(media>=7):
	print(round(media,2))
	print("Aprovacao")
if(media<7):
	print(round(media,2))
	print("Reprovacao por nota")