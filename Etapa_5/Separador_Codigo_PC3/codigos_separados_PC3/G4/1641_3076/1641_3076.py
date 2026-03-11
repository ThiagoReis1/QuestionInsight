from numpy import*

v = array(eval(input("")))

x = 0

for i in range(size(v)):
	if(v[i]%3 == 0):
		x = x + 1
		
n = zeros(x, dtype=int)
j = 0

for i in range(size(v)):
	if(v[i]%3 == 0):
		n[j] = i 
		j = j + 1
	
print(x)
print(n)