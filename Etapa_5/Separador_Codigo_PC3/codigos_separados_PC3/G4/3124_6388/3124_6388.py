from numpy import*

m = array(eval(input(":")))
k = 1

for i in range(len(m)):
	k = m[i]*k
	
d= k**(1/size(m))
print(round(d,2))