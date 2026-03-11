from numpy import*
nota=array(eval(input()))
rp=0; ind=[]
for i in range(size(nota)):
	if nota[i]>=70:
		rp=rp+1
		ind.append(i)
u=zeros(size(ind), dtype=int)
u=u+ind
print(rp)
print(u)
#from numpy import*
#r=0
#k=[]
#v=array(eval(input("vetor: ")))
#for i in range(size(v)):
#	if (v[i]70):
#		r=r+1
#		k.append(i)
		
#l=zeros(size(k), dtype(int))
#l=l+k
#print(r)
#print(l)