from numpy import*
nota=array(eval(input()))
rp=0; ind=[]
for i in range(size(nota)):
	if nota[i]<70:
		rp=rp+1
		ind.append(i)
u=zeros(size(ind),dtype=int)
u=u+ind
print(rp)
print(u)