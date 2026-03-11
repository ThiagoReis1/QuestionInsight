from numpy import*
v= array(eval(input("")))
p =0
for i in range(size(v)):
	if(v[i] % 2 !=0):
		p = p+1
u= zeros(p,dtype=int)
j= 0
for i in range(size(v)):
	if(v[i] % 2 !=0):
		u[j]= i
		j= j+1
	
	
print(p)
print(u)