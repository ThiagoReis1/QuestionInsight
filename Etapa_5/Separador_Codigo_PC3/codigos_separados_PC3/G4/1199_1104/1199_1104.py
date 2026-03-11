from numpy import*
vt=array(eval(input()))
vtn=zeros(size(vt),dtype=float)
i=0
j=0
while(i<size(vt)):
	while(vt[i]>=0):
		if(vt[i]>10 and vt[i]<40):
			vtn[j]=vt[i]
			i=i+1
			j=j+1
		else:
			i=i+1
print(vt)

		