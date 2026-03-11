from numpy import*
v=array(eval(input("frequencia: ")))
rp=0; ind=[]
for i in range(size(v)):
	if v[i]<70:
		rp=rp+1
		ind.append(i)
u=zeros(size(ind),dtype=int)
u=u+ind
print(rp)
print(u)