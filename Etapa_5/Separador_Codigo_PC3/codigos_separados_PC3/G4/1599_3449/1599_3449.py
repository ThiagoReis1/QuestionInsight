from numpy import*
v= array((eval(input("compras: "))))

for i in range(size(v)):
	if (v[i]>80):
		b=sum(v)-((15)/100)
	else:
		b=sum(v)
print(round(b,2))
	