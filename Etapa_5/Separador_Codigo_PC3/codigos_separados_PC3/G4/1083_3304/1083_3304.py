p1 = float(input("nota1: "))
p2 = float(input("nota2: "))
p3 = float(input("nota3: "))
x= (p1+p2+p3)/3

if(x>=6):
	print(round(x,2))
	m = ("Aprovacao")
	print(m)
else:
	print(round(x,2))
	m = ("Reprovacao")
	print(m)