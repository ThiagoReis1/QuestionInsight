from numpy import*
v=array(eval(input("valor de N:")))

acu=0
for i in range (size(v)):
	c=log(v[i]+1)
	acu=acu+c
	
div=acu/size(v)
m=exp(div)-1

print(round(m,2))