num = int(input("qual o numero:"))
a = num // 100
restoa = num % 100
b = restoa // 10 
restob = restoa % 10
c= restob
X = a**3 + b**3 + c**3
if (X == num):
	print(X , ("atende a propriedade"))
else:
	print(X)
