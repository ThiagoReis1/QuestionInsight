n1= float(input("prova 1: "))
n2= float(input("prova 2: "))
n3 = float(input("prova 3:"))

x= n1+n2+n3
y= x/3
if(y >= 6):
	print(round(y,2))
	print("Aprovacao")
else:
	print(round(y,2))
	print("Reprovacao")
