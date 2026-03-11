from numpy import *
v=zeros(4,dtype=int)
cat="EVAD"
u=input("")

for i in range(0,len(u)):
	for j in range(0,4):
		if u[i]==cat[j]:
			v[j]+=1
print(v)
