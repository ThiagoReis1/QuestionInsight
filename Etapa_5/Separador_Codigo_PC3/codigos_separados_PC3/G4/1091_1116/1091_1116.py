a = int(input("digite o numero"))
b = a % 100
c = a // 100
if(a == (b + c)**2):
	print(a ,"atende a propriedade")
else:
	d = (b + c)**2
	print(d)