from numpy import*

vet = array(array(eval(input(" : "))))
c = 0

for i in vet:
	if (i%2==0):
		c = c + 1

v = zeros(c, dtype= int)
j = 0
k =0

for i in vet:
	if (i%2==0):
		v[k] = j
		k = k + 1
	j = j + 1
print(c)
print(v)