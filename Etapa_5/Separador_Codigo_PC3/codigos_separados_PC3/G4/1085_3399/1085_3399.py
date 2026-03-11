n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
n3 = float(input("terceira nota: "))
n4 = float(input("quarta nota: "))
n5 = float(input("quinta nota: "))

ad = (n1 + n2 + n3 + n4 + n5)/5

if(ad >= 6.0):
	print(round(ad, 2))
	print("Aprovacao")
else:
	print(round(ad, 2))
	print("Reprovacao")