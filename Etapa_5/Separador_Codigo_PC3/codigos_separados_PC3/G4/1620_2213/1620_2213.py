from numpy import *
vt=array(eval(input()))
tp=array(eval(input()))
i=0
soma=0
while(i<size(vt)):
	soma=soma+(5*(tp[i]/100))*vt[i]
	i=i+1
print(soma)
	