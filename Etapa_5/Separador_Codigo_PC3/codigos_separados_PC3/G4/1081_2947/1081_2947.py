n1 = float(input(":"))
n2 = float(input(":"))
n3 = float(input(":"))
n4 = float(input(":"))

media = (n1 + n2 + n3 + n4) / 4

if(media >= 5):
	print(round(media, 2))
	print("Aprovacao")
else:
	print(round(media, 2))
	print("Reprovacao")
