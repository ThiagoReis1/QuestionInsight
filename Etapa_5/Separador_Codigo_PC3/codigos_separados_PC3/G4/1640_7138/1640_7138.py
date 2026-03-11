from numpy import*
t = array(eval(input()))

i = 0 
c = 0 
a = 0 
d = 0 

while(i<size(t)):
	if(t[i]%2 != 0):
		c = c + 1
	i = i + 1
print(c)

v = zeros(c, dtype=int)

for a in range(size(t)):
	if(t[a]%2 != 0):
		v[d] = a
		d = d + 1
print(v)