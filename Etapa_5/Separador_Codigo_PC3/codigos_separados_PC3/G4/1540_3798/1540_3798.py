from math import*
x=eval(input("angulo "))
k=int(input("quantidade "))
soma=0
while(k<=soma):
	if(x>=0 and k>0):
		cos=1+(((-1)**k)*x/2*k)
		soma=soma+1
	print(round(cos,6))