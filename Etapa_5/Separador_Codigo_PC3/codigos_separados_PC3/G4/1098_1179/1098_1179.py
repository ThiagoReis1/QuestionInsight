x=int(input("inserir valor"))
a=x//1000
b=x%1000
c=(a-b)**4
if (c==x) :
	print (x, "atende a propriedade")
else:
	print (c)