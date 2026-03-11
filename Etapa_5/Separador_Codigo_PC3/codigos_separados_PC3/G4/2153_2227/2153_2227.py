from numpy import*

p1=array(eval(input("vetor p: ")))
q1=array(eval(input("vetor q: ")))
d=0

for i in range(size(q1)):
	d=d+(p1[i]-q1[i])**2
a=sqrt(d)
b=round(a,4)
print(b)