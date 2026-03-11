from numpy import *
n=array(eval(input("")))
i=0
soma=0

while(size(n)>i):
	if(n[i]>=4 and n[i]<=5):
		n[i]=4
	elif(n[i]>=9 and n[i]<=10):
		n[i]=10
	i=i+1
print(n)