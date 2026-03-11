from numpy import*
v= array(eval(input("Digite o vetor: ")))
x= 40
i=0
c=0
while i<size(v):
	if (v[i]<x):
		c=c+1
		a=v[i]
		print(a)
	i=i+1
	while i<size(a):
		if (a<x):
			c=c+1
		i=i+1
print("[",a,"]")