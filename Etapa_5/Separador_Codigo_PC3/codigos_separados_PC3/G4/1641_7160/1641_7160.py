from numpy import*

v = array(eval(input()))

n = 0
vet = []

for i in range (size(v)):
	if(v[i]%3 == 0):
		n = n + 1
		vet.append(i)
print(n)
print(array(vet))