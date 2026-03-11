from numpy import*
v=array(eval(input("andares:")))

i=1;
n=0;
while i<size(v):
	n= n + abs(v[i]- v[i-1])
	i=i+1
print(n)
