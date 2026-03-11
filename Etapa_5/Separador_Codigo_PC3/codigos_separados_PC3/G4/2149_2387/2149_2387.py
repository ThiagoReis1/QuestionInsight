from numpy import*
n1 = array(eval(input()))
n2 = array(eval(input()))
d = zeros(size(n1))
for a in range(size(n1)):
	d[a] = n1[a] + n2[a]
print(d)	
i = 0
for a in range(size(n1)):
	if(n1[a]+n2[a] >= 12):
		i = i + 1
print(i)		