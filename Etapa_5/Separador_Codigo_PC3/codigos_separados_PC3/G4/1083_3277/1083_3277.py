a=float(input("Nota 1: "))
b=float(input("Nota 2: "))
c=float(input("Nota 3: "))
M= (a+b+c)/3
if (M>=6):
	print(round(M,2))
	print("Aprovacao")
else:
	print(round(M,2))
	print("Reprovacao")