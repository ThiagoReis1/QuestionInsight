prova1=float(input(""))
prova2=float(input(""))
prova3=float(input(""))
prova4=float(input(""))
prova5=float(input(""))

media=(prova1+prova2+prova3+prova4+prova5)/5

if (media>=6.0):
	print(round(media, 2))
	print("Aprovacao")
	
else :
	print(round(media, 2))
	print("Reprovacao")