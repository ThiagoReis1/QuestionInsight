from numpy import*
n =array(eval(input()))

i=0
c=0
p=1

while (i<size(n)):
	c=c+(i+1)*n[i]
	i =i +1
x=arange(i+1)
m = c/ sum(x)
print(round(m,2))
