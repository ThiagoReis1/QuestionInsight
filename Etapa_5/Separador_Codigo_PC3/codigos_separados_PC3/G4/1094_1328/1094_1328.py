n1=int(input("informe valor:"))
n2=n1//100000
n3=n1%100000
soma=((n2+n3)**2)
if(n1==soma):
	print(n1,"atende a propiedade")
else:
	print(soma)