from numpy import*
nota=array(eval(input("notas: ")))
ap=0
ind=[]
for i in range(size(nota)):
	if nota[i]>=5.0:
		ap=ap+1
		ind.append(i)
u=zeros(size(ind),dtype=int)
u=u+ind
print(ap)
print(u)