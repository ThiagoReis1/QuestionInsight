n=int(input("informe um Nº:"))

q=n//1000
y=n%1000
x=(q-y)**4
if(n==x):
	print(n,"atende a propriedade")
else:
	print(x)
