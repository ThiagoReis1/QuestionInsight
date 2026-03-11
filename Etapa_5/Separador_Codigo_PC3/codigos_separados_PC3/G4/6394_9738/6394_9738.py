from numpy import*

n= array(eval(input()))
v= zeros(size(n),dtype=int)

for i in range(size(n)):
	if n[i]==9:
		v[i]= 0**3
	else:
		v[i]= (n[i]+1)
print(v)