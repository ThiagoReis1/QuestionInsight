from numpy import *
freq=array(eval(input("frequencia")))
rep=zeros(1,dtype=int)
for i in range(0,size(freq)):
	if freq[i]<70:
		rep[0]=rep[0]+1
	else:
		rep[1]=rep[1]+0
	print(rep)	