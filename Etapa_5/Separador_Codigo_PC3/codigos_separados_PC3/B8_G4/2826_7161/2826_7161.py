from numpy import*
x = array(eval(input("nota: ")))
i = 0
while i<size(x):
	if 8.0<x[i]:
		x[i]=10.0
	elif x[i]<2.0:
		x[i]=0.0
	i=i+1
	
print(x)
