n1=float(input(":"))
n2=float(input(":"))
n3=float(input(":"))
n4=float(input(":"))
n5=float(input(":"))

ma= (n1+n2+n3+n4+n5)/5

if(ma>=6):
	print(round(ma,2))
	print("Aprovacao")
else:
	print(round(ma,2))
	print("Reprovacao")