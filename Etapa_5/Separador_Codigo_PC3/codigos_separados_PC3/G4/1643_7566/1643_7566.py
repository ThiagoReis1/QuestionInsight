from numpy import *
a = array(eval(input("insira as notas: ")))
j = 0
for i in range(size(a)):
	if(a[i] >= 5):
		j += 1
b = zeros(j, dtype = int)
l = 0
for k in range(size(a)):
	if(a[k] >= 5):
		b[l] = k
		l += 1
print(j)
print(b)
	