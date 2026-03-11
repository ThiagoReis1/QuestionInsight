from numpy import*

v = array(eval(input()))

s = 0
t = 0 
for i in range(size(v)):
	if(v[i] % 5 == 0):
		s = s +1
print(s)

x = zeros(s, dtype = int)

for j in range(size(v)):
	if(v[j] % 5 == 0):
		x[t] = j
		t = t + 1
print(x)