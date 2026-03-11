n1 = float(input("valor da n1: "))
n2 = float(input("valor da n2: "))
n3 = float(input("valor da n3: "))
n4 = float(input("valor de n4: "))

media = (n1 + n2 + n3 + n4)/ 4
if(media>=5):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao")