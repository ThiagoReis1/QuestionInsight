from numpy import*
a = array(eval(input("%: ")))
k = 0
d = 0
e = 0
for i in a:
	if(i<70):
		k = k + 1
b = zeros(k, dtype=int)
for n in a:
	if(n<70):
		b[d] = e
		d = d + 1
	e = e + 1
print(k)
print(b)