from numpy import*

v = array(eval(input(": "))) 
b = ones(v, dtype=int)
j = 0
c= 0
b= 0
a = 0
for i in range(size(v)):
	if ( v[i] == 0 ):
		j = j + 1
	elif (v[i] == 1):
		c = c + 1
	elif (v[i] == 2):
		b = b + 1
	elif (v[i] == 3):
		a = a + 1
		
print(j, b, a, c)			