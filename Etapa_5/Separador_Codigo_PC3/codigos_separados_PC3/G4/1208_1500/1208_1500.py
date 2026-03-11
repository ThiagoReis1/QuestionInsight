from numpy import*
x=array(eval(input("numero da distancia de lançamentos:")))
i=0
k=0
r=98.48
while(i>size(x)):
	if(x[i]<r):
		k= k+ 1
	i= i + 1
print(r)
print(k)