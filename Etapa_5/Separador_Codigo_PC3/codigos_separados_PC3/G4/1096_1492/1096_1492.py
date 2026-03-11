x =int(input("digite o numero:"))
a = x % 1000 , x // 1000
b = a % 100 , a // 100
c = b % 10 , b // 10

if (x == a**3 + b**3 + c**3):
	print(x)
else:
	print(a)