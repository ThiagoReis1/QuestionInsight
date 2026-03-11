n = int(input("digite o valor do numero:"))
n1 = n//10000
nresto = n%10000
if (n==(n1+ nresto)**2):
	print (n, "atende a propriedade")
else:
	print ((n1+nresto)**2)