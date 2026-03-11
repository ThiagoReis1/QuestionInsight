n1= float(input("Insira a n1: "))
n2= float(input("Insira a n2: "))
n3= float(input("Insira a n3: "))
n4= float(input("Insira a n4: "))
n5= float(input("Insira a n5: "))

media= (n1+n2+n3+n4+n5)/5.0

if(media >= 7.0):
	print(round(media, 2))
	print("Aprovacao")
else:
	print(round(media, 2))
	print("Reprovacao")