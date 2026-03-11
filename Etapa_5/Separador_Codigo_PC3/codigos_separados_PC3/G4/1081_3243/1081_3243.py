n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

m = (n1 + n2 + n3 + n4) / 4

if(m >= 5):
	print(round(m, 2))
	print("Aprovacao")
	
else:
	print(round(m, 2))
	print("Reprovacao")