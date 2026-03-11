from numpy import*
x=input().upper()
v=[]
w=["A","E","I","O","U"]
i=0
while i<len(x):
	if x[i] in w:
		v.append(x[i])
	i=i+1
p=size(v)
print((len(x)-p)*0.17+p*0.15)