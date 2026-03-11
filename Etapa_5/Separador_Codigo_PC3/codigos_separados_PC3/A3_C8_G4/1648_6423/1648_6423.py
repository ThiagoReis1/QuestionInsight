from numpy import*
v = array(eval(input("")))
x = 0

a = 0

s = 0

for i in range(size(v)):
	if v[i]<70:
		x = x+1
	i+=1
z = zeros(x, dtype=int)
for j in range(size(v)):
	if v[j]<70:
		v[a] = j
	a+=j




print(x)
print(v)
print(j)