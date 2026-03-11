
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

m = (n1 + n2 + n3 + n4 + n5)/5

if(m>=7.0):
	print(round(m,2))
	print("Aprovacao")
else:
	print(round(m,2))
	print("Reprovacao por nota")
