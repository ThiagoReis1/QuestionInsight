from numpy import*
n = array(eval(input()))
p = sum(n)
n5 = 0
for i in range(size(n)):
	if(n[i]>=5):
		n5 = n5+1
print(p)
print(n5)