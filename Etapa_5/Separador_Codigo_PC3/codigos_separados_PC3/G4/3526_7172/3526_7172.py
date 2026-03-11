x=float(input("numero:"))
k=int(input("quantidade de termos:"))
d=1
cont=1
arc=0
if(x>-1 and x<1):
	if(k>0):
		while(cont<=k):
			arc=arc+(x**d)/d
			d=d+2
			cont=cont+1
print(round(arc,7))
