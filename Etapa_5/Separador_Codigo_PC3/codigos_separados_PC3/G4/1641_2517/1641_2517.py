from numpy import*
v = array(eval(input()))
i = 0
for x in range(size(v)):
	if(v[x]%3 == 0):
		i=i+1
print(i)
j=0
y = zeros(i, dtype=int)
for x in range(size(v)):
	if (v[x]%3 == 0):
		y[j] = x
		j=j+1
print(y)