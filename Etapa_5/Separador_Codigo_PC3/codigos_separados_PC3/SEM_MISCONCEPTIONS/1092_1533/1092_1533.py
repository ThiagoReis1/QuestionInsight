num = (int(input("qual o valor do numero ? ")))

x = num //100
resto_x = num % 100
y = resto_x //10
resto_y = resto_x % 10
k = resto_y
total = x**3 + y**3 + k**3
if (num == total):
	print(num , "atende a propriedade")
else:
	print(total)