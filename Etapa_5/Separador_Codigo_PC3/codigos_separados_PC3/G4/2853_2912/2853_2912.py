from numpy import *
arr = array(eval(input()))
soma = 0 
for i in arr:
	soma+=i
	if(i==10):
		soma-=i
		soma*=10
print(soma)