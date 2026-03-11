from numpy import*
a = array(input().split(","))
b = zeros(5,dtype = int)
c = array(["BE","ES","FR","IT","PT"])

for i in range (size(a)):
	for j in range (size(c)):
		if(a[i].upper() == c[j]):
			b[j] = b[j] + 1
print(max(b))
print(b)