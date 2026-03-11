from numpy import * 

b = array(eval(input()))
m = 0
p = 0
for i in range(size(b)):
	if b[i] < 70:
		m = m + 1
y = zeros(m,dtype=int)
for j in range(size(b)):
	if b[j] < 70:
		y[p] = j
		p = p + 1
print(m)
print(y)



