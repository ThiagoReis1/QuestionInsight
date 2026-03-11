n1=float(input("nota 1:"))
n2=float(input("nota 2:"))
n3=float(input("nota 3:"))
n4=float(input("nota 4:"))
n5=float(input("nota 5:"))
x=(n1+n2+n3+n4+n5)/5
if(x>=7.0): 
	print(round(x,2))
	print("Aprovacao")
else:
	print(round(x,2))
	print("Reprovacao por nota")