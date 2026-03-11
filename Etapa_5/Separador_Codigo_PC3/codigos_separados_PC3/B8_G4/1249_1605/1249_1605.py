from numpy import*
v=array(eval(input("digitr vetor")))
b=max(v)
a=min(v)
c=0.7*a+0.3*b
d=0.4*a+0.6*b
m=0
n=0
for i in v:
	if i>=a and i<c:
		m=m+1
	elif i>=c and i<d:
		n=n+1
k=array([m,n])
print(k)