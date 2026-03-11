X = int(input())

a = X // 100
restoX = X % 100
b = restoX // 10
restoB = restoX % 10
c = restoB

if(X == (a**3 + b**3 + c**3)):
	print(X," atende a propriedade")

else:
		s = a**3 + b**3 + c**3
		print(s)
	