from numpy import*
v = array(eval(input()))
a = zeros(size(v)-1, dtype=int)
z = 0
y = 1
for i in a:
	a[z] = v[y]
	z = z + 1
	y = y + 1
q = 0
x = 1
for elemento in a:
	if(elemento>=v[0]):
		print(x)
		x = x + 1 
		q = q + 1
	else:
		x = x + 1
print(q)