from numpy import*

v = array(eval(input(": ")))
s = 0
for i in range(size(v)):
	if (v[i] <= 50):
		s = s + 1 
print(s)
j = -1
b = zeros(s, dtype=int)
for i in range(size(v)):
	if (v[i] <= 50 ):
		b[j] = i
print(b)