x = int(input("insira um numero: "))

a = int(x/1000.0)
b = int(a%1000.0)
c = int((a+b)**2)

if (x == c):
	print("X atende a propriedade")
	print(c)
else:
	print (c)
