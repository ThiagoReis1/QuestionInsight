from numpy import * 

a = array(eval(input()))


reprov = 0

for i in range(size(a)):
	if a[i] < 5 :
		reprov = reprov + 1
print(reprov)

n = zeros(reprov,dtype=int)
b = 0
for i in range (size(a)):
	if a[i] < 5:
		c = i
	
print(n)