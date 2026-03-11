x = int(input("digite um numero de seis digitos: "))

a = x // 10000
b = x % 10000
c = b // 100
d = b % 100
j = (a**3)+(c**3)+(d**3)

if(x == j):
	print("atente")
	print(x)
else:
	print("nao atende")
	print(x)