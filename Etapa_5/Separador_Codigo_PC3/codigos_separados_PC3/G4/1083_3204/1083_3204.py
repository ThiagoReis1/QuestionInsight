p1 = float(input("primeira nota:"))
p2 = float(input("segunda nota:"))
p3= float(input("terceira nota:"))
ma = (p1+p2+p3)/3
if(ma>=6):
	print(round( ma, 2))
	print("Aprovacao")
else:
	print(round(ma, 2))
	print("Reprovacao")