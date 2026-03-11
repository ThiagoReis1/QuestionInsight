from numpy import * 

a = array(eval(input('Determine o n de aulas assistidas: ')), dtype=int)

c = 0

for i in range(size(a)):
	if a[i] < 70:
		c += 1
		
print(c)

j = 0
v0 = zeros(c, dtype=int)

for i in range(size(a)):
	if a[i] < 70:
		v0[j] = i
		j += 1

print(v0)