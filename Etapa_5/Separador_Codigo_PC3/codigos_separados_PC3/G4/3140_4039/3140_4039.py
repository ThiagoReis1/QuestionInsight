from numpy import*
v = array(eval(input()))
n = size(v)
i=0
m1=0
while(i<size(v)):
	m=v[i]**(5)
	m1=m1+m	
	i=i+1
t = m1 / n
t1 = t ** (1/5)
print(round(t1, 2))