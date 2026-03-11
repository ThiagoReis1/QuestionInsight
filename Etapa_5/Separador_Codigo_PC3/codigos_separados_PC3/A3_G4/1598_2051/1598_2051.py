from numpy import*

v = array(eval(input("v: ")))
i=0
x=0
p=0
#custo total de compras:
while (i< size(v)):
	if (v[i]>80):
		x=x+1
		i=i+1
	else:
		i=i+1
		
final= sum(v)-x*5 
print(round(final,2))
