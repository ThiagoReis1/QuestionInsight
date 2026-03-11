from numpy import*
v=array(eval(input()))

p=[2,1,5]
x=0
s=0

while x!=size(v):
	s+=p[x]*v[x]
	x+=1
print(round(s/sum(p),2))