from numpy import*

n = array(eval(input()))

i = 0 
c = 0 
while(i<size(n)):
	if(n[i]%2!=0):
		c = c + 1
	i = i + 1
print(c)
z = zeros(c,dtype=int)
k = 0 
j = 0 
while(j < size(n)):
	if(n[j]%2 != 0):
		z[k] = j
		k = k + 1
	j = j + 1
print(z)	