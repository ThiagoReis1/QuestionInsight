from numpy import *
v = array(eval(input("compras: ")))
q = size(v)
p = 0
d = 0
s = sum(v)

while p <= q - 1:
	if v[p] > 160:
		d = d + 25
	p = p + 1
		
ct = s - d
print(round(ct,2))
			 
