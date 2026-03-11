from numpy import*
v = array(eval(input("")))
z = 1
i = 0
while i < size(v):
	nt = v[i] * z
	z = z + 1
	i = i + 1
	
print(round(nt/v , 2))