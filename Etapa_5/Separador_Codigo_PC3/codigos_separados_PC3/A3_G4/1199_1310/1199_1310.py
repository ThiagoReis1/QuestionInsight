from numpy import *
e=array(eval(input("w: ")))
i=0
j=0
while i<size(e):
	if e[i]>=10 and e[i]<=40:
		j=j+1
	i=i+1
v=array(zeros(j, dtype=float))
k=0
g=0
n=0
while g<size(e):
	if e[g]>=10 and e[g]<=40:
		v[n]=e[g]
		n=n+1
	g=g+1
print(v)
49.3,27.5,27.7,28.1,-2.3,28.2