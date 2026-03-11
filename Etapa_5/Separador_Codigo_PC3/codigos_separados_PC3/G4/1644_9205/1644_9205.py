from numpy import*
a = array(eval(input()))
r = 0
ind = []
for i in range(size(a)):
	if(a[i] < 5):
		r += 1
		ind.append(i)
print(r)
print(array(ind))

