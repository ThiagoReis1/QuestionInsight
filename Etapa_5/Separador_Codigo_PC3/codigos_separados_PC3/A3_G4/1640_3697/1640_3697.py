from numpy import*

v=array(eval(input("v:")))
qi=0
i=0
a=0
j=0
while(size(v)>i):
	if(v[i]%2==1):
		qi=qi+1
	i=i+1
print(qi)
