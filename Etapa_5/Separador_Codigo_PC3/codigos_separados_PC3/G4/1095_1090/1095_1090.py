x = int(input())

a = x // 10000
b = x % 10000
d = (a+b)**2

if( x == d ):
	print(x,"atende a propriedade")
	
else:
	print(d)