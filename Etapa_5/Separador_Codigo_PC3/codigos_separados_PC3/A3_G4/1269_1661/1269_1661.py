from numpy import*
p=float(input())
x=array(eval(input()))
y=array(eval(input()))
t=p/(p+1)
s=0
for i in range(size(x)):
	sa= (abs(x[i]+y[i]))**t
	s= (abs(x[i]-y[i]))**t
h= (sa - s)

d=(h)**(1/t)

print(round(d, 7))