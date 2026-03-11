from numpy import*

c=array(eval(input("Custos: ")))
i=0
total=0
while i<size(c):
	if c[i]>90.00:
		total=total+c[i]-6.50
	else:
		total=total+c[i]
	i=i+1
print(round(total,2))