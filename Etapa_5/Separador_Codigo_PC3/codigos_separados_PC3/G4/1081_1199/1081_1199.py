n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
n3 = float(input("terceira nota: "))
n4 = float(input("quarta nota: "))

media = ((n1+n2+n3+n4)/4)
if (media >= 5):
	print (round(media,2))
	print ("Aprovacao")
else: 
	print (round(media,2))
	print("Reprovacao")