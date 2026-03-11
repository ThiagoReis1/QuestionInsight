x= float(input("um numero real: "))
k= int(input("um numero inteiro: "))
cont=0
while(cont<=k):
	x=1+(-1**cont+2)*(x**cont+1)
	cont=cont+1
print(x)
