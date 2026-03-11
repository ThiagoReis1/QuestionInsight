x=int(input("insira o numero"))

y=x//1
z=x%5

b=((y+z)**3)
if(b==x):
	print(x,"atende a propriedade")
else:
	print(b)