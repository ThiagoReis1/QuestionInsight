from numpy import*
x=array(eval(input(":")))
so=0
for i in range(size(x)):
	if(x[i]!=88):
		so=so+x[i]
	else:
		so=so/2
print(round(so,2))
	