from numpy import*
n= array(eval(input(":")))
rp = 0
ind = []

for i in range(size(n)):
	if n[i]%2!=0:
		rp=rp+1
		ind.append(i)
		
u= zeros(size(ind), dtype=int)
u= u+ind

print(rp)
print(u)