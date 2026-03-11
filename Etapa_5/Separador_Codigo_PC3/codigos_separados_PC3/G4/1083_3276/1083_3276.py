p=float(input("nota"))
p1=float(input("nota"))
p2=float(input("nota"))

n=(p+p1+p2)/3

if(n>6):
	print(round(n,2))
	print("Aprovacao")
else:
	print(round(n,2))
	print("Reprovacao")