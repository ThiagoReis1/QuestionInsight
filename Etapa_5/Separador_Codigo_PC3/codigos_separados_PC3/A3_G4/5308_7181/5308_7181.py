x=float(input("numero real:  "))
k=int(input("quantidade de termos:  "))
cont=1
m=2
s=0
if(k!=0):
	if(x!=0):
		while(cont<=k):
			s=cont/(m*x)
			cont=cont+1

print(round(s, 10))
