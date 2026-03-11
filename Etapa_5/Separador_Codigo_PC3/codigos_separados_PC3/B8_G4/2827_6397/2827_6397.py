from numpy import*
x=array(eval(input("nota: ")))
i = 0
while i<size(x):
	if 4<=x[i]<=5:
		x[i]=4.0
	elif 9<=x[i]<=10:
		x[i]=10.0
	i=i+1
print(x)