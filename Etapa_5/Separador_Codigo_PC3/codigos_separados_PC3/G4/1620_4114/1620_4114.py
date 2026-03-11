from numpy import*
a=array(eval(input("Tempo: ")))
b=array(eval(input("Percentual")))
i=0
x=0
while(i<size(b)):
	x+=(b[i]*5/100)*a[i]
	i=i+1
print(round(x,2))	