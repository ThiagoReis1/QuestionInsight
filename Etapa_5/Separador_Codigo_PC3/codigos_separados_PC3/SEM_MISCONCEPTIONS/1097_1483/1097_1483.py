#entrada
v = 132496 = 
v = int(input("digite entrada:"))
x1 = v // 1000
x2 = v % 1000

if(v == (x1 - x2)):
	print(v , "X atende a propriedade")
else:
	y = (x1 - x2)**2
	print(y)