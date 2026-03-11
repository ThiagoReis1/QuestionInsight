from numpy import*
v = array(eval(input('vet: ')))

a = zeros(size(v),dtype = int)

for i in range(size(v)):
	a[i] = v[i]**2
print(a)
