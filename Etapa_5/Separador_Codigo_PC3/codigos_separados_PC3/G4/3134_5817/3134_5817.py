from numpy import*

v=array(eval(input("Vetor: ")))
i=0
n=size(v)
c=0
while i<n:
	c=c+(v[i]**2)
	i=i+1
m=(c/n)**(1/2)
print(round(m,2))