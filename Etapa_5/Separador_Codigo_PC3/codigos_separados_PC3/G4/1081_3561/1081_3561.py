n1=float(input("leia a nota:"))
n2=float(input("leia  a nota:"))
n3=float(input("leia  a nota:"))
n4=float(input("leia  a nota:"))
mf=(n1+n2+n3+n4)/4
if (mf>=5):
	print(round( mf,2))
	print("Aprovacao")
else:
		print(round(mf,2))
		print("Reprovacao")