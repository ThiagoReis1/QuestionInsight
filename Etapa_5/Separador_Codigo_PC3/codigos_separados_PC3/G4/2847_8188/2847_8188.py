from numpy import*

v=array(eval(input("digite ")))

num=zeros(size(v),dtype=int)



for i in range(size(v)):
	num[i]=v[i]**2
	
print(num)