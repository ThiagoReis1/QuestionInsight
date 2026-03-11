x = int(input("digite um valor: "))
x1 = x // 100 
x2 = x % 100
if(x == (x1 + x2)**2):
	print(x, "atende a propriedade")
else:
	print((x1 + x2)**2)
