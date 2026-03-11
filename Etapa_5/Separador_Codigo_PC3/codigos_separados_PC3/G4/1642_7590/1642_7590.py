from numpy import*
v = array(eval(input("")))
ms = 0

for i in range(size(v)):
	if(v[i]%5==0):
		ms = ms + 1
print(ms)

j=0
p = zeros(ms, dtype=int)
for i in range(size(v)):
	if(v[i]%5==0):
		p[j] = i
		j = j + 1
			
print(p)
