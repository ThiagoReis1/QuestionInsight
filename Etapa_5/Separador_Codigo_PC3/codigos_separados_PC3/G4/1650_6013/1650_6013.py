from numpy import*

a = array(input().split(","))
b = zeros(5,dtype=int)
c = array(["P","C","R","L","B"])

for i in range(size(a)):
	for j in range(size(c)):
		if(a[i].upper()==c[j]):
			b[j] = b[j]+1
print(max(b))
print(b)