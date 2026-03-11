n1 = float(input("digite a nota 1:"))
n2 = float(input("digite a nota 2:"))
n3 = float(input("digite a nota 3:"))
ma = round((n1+n2+n3)/3,2)
if (ma >= 6):
	print(ma)
	print("Aprovacao")
else:
	print(ma)
	print("Reprovacao")
	