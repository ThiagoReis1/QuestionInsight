from numpy import*
al = array(eval(input()))
ti=0
for i in range(size(al)):
	if(al[i]%2 !=0):
		ti= ti+1
a=ti

print(a)
v= zeros(a, dtype=int)
ps=0

for i in range(size(al)):
	if(al[i]%2 !=0):
		v[ps]= i
		ps = ps+1
	
print(v)