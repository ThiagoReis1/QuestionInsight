from numpy import *
a=array(eval(input("digite os coef. : ")))
b=""
i=0
j=size(a)-1

while(i<size(a)-2):
	b=b + str(a[i])+"x^"+str(j)+" + " 
	i=i+1
	j=j-1

if(size(a)==1):
	b=str(a[0])
else:
	b=b+ str(a[-2])+"x + "+ str(a[-1])
print(b)
	