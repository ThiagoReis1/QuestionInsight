from numpy import*

v = array(eval(input(": ")))
acum = 0
a = 0
for i in range(size(v)):
	if v[i] <= 50:
		acum = acum + 1

r = zeros(acum, dtype = int)

for i in range(size(v)):
	if v[i] <= 50:
		r[a] = i
		a = a + 1
		
print(acum)
print(r)