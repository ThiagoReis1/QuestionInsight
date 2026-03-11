from numpy import*
p=float(input())
x=array(eval(input()))
y=array(eval(input()))
t=p/(p+1)
s=0
for i in range(size(x)):
	s+=abs(2x[i])**t:
	s+=abs(3y[i])**t:
d=(s)**(1/t)
print(round(d,7))