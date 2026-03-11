v = int(input())

x=v//100
y=v%100

x2=x*x
y2=y*y

if x2+y2==v:
	print( v,"atende a propriedade")
else:
	print(x2+y2)

	