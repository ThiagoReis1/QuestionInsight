x = int(input("digite um numero:"))
w = x // 10000
resto_w = x % 10000
y = resto_w // 100
resto_y = resto_w % 100
b = resto_y // 1
r = w**3 + y**3 + b**3
if(r == x):
	print(x,"atende a propriedade")
else:
	print(r)