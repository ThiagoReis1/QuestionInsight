n1 = float(input("prova I "))
n2 = float(input("prova II "))
n3 = float(input("prova II "))
n4 = float(input("prova IV "))
n5 = float(input("prova V "))

ma = (n1 + n2 + n3 + n4 + n5) / 5

if (ma >= 7):
	print(round(ma, 2))
	print("Aprovacao")
else:
	print(round(ma, 2))
	print("Reprovacao por nota")