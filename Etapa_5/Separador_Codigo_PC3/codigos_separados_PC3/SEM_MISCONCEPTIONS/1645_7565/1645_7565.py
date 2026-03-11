from numpy import*
s=array(eval(input(": ")))
cont=0
n=zeros(s,dtype=int)
for i in range(0,size(s)):
	if(s[i]>=2000):
		cont[i]=cont[i]+1
	if(s[i]==2000):
		cont[i]=cont[i]+1
	else:
		