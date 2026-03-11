from numpy import*

sn=array(eval(input()))
sw=zeros(size(sn), dtype=int)

for i in range(size(sn)):
	if sn[i]==0:
		sw[i]=9**3
	else:
		sw[i]= (sn[i]-1)**3
print(sw)