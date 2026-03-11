from numpy import*
a=array(eval(input("")))
c=0
for i in range(size(a)):
	if a[i]>=70:
		c+=1
print(c)
z= zeros(c, dtype=int)
j=0
for i in range(size(a)):
	if a[i]>=70:
		z[j]=i
		j+=1
print(z)