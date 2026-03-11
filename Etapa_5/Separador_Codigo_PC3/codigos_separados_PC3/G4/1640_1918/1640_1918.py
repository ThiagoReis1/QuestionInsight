from numpy import*
v = array(eval(input("")))
c = 0
for i in range(size(v)):
	if(v[i]%2 != 0):
		c = c + 1
newv= zeros(c, dtype=int)
i = 0		
for j in range(size(v)):
	if(v[j]%2 != 0):
		newv[i] = j
		i = i + 1
print(c)
print(newv)