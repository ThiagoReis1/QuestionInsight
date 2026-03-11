from numpy import*
a=array(eval(input()))
i=0
s=0
while i<size(a):
	if a[i]>80:
		a[i]=a[i]-a[i]*0.15
	i=i+1
print(round(sum(a),2))