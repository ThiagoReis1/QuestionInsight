from math import*

x=float(input( ))
k=int(input( ))

cont=2
cont2=0
soma=1/1

while cont2<k:
	a=x**(cont)
	b=factorial(cont)
	y=a/b
	soma=soma+y
	cont=cont+2
	cont2=cont2+1
print(round(soma,8))