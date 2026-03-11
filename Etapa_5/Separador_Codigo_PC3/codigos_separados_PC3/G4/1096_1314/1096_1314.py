x=int(input("digite um numero x:"))
a=x//10000
b=(x%1000)//100
c=(x%100)%100
s=a**3+b**3+c**3
if(s==x):
	print(x,"atende a propriedade")
else:
	print(s)
	