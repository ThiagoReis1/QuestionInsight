from math import*

x=eval(input("Insira o angulo em radianos: "))
k=int(input("Qual a quantidade de termos de serie?"))
n=0
a=2
cos=1

if(k==1):
	print(cos)
else:
	while(n<k):
		