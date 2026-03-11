X = int(input())
a = X//100
b = (X%100)//10
c = (X%100)%10
if X == a**3 + b**3 + c**3:
	print(X ,"atende a propriedade")
else:
	print(a**3 + b**3 + c**3)