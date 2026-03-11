n=int(input("digite o número: "))
x=n//10000
y=x%10
z=(x+y)
soma=x*3+y*3+z*3
if(n==soma):
	print(n ,"atende a propriedade")
else:
	print(soma)