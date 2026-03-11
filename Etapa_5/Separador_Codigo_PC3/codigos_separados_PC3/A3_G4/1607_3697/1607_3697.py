from numpy import*

a = array(eval(input()))
i=1
d=0
q=0
while(i<size(a)):

	q= a[i]
	d= abs(q-a[i-1])*3 +d
	i=i+1
	
print(d)
