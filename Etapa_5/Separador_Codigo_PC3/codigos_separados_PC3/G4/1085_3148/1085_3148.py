n1=float(input("n1:"))
n2=float(input("n2:"))
n3=float(input("n3:"))
n4=float(input("n4:"))
n5=float(input("n5:"))

x=(n1+n2+n3+n4+n5)/5
if(x>=6.0):
	print(round(x,2))
	print("Aprovacao")
else:
	print(round(x,2))
	print("Reprovacao")
	