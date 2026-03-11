from numpy import *
v=input().upper().split(',')
g=zeros(5, dtype=int)
i=0
while i< len(v):
	if v[i]== "P":
		g[0]=g[0]+1
	elif v[i]=="C":
		g[1]=g[1]+1
	elif v[i]=="R":
		g[2]=g[2]+1
	elif v[i]== "L":
		g[3]=g[3]+1
	elif v[i]== "B":
		g[4]=g[4]+1
	i+=1
print(max(g))
print(g)

