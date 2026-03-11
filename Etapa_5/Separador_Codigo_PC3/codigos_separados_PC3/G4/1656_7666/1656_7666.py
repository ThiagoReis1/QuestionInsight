from numpy import*

a = array(input().split(","))
b = array(["BE","ES","FR","IT","PT"])
c = zeros(size(b),dtype = int)

for i in range(size(a)):
	for j in range(size(b)):
		if(a[i].upper() == b[j]):
			c[j] = c[j] + 1
			
print(max(c))
print(c)