from numpy import*
p= float(input())
x=array(eval(input()))
y=array(eval(input()))
p=p/(p+1)
s=0
t=0
for i in range (0,size(x)):
	s= s +(abs(x[i]+y[i]))**p
s = s**(1/p)
for i in range (0,size(x)):
	t= t +(abs(x[i]-y[i]))**p

t = t**(1/p)
print(round(s-t,7))