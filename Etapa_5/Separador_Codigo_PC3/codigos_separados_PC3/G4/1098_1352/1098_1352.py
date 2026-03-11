x=int(input("informe o numero:"))
k=x//1000
k1=x%1000
conta=((k-k1)**4)
if(conta==x):
	print(x,"atende a propriedade")
else:
	print(conta)