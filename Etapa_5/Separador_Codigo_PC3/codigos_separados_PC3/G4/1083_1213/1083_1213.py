n1 = float(input("N1:"))
n2 = float(input("N2:"))
n3 = float(input("N3:"))
md = (n1+n2+n3)/3
if (md >=6):
	print(round(md,2))
	print("Aprovacao")
else:
	print(round(md,2))
	print("Reprovacao")