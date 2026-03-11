from numpy import*
x=array(eval(input("insira as notas: ")))
i=0
while i<size(x):
	if x[i]>8:
		x[i]=10.0
	elif x[i]<2:
		x[i]=0.0
	i=i+1
print(x)	