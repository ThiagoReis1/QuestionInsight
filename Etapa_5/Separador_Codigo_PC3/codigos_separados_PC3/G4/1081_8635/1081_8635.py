
nt1 = float(input("nota 1: "))
nt2 = float(input("nota 2: "))
nt3 = float(input("nota 3: "))
nt4 = float(input("nota 4: "))
media = (nt1+nt2+nt3+nt4)/4

if media >= 5.0:
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print ("Reprovacao")
