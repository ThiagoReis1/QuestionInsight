n1 = float(input("valor de n1: "))
n2 = float(input("valor de n2: "))
n3 = float(input("valor de n3: "))
ma = (n1 + n2 + n3)/ 3
if ( ma >= 6.0 ):
	print(round(ma, 2))
	print("Aprovacao")
else:
	print(round(ma, 2))
	print("Reprovacao")