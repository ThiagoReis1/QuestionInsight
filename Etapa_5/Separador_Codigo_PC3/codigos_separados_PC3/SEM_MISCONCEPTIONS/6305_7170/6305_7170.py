a = input("H, L ou E: ")
h = 0
l = 0
e = 0
v = 0
i = 0
while a[i]  "HLE":
	for a in "H":
		h = h+1
		v = v+h*3.85
		
	for a in "L":
		l = l+1
		v = v+l*2.95
	for a in "E":
		e = e+1	
		v= v+e*7.90

	i += 1
	
print(round(v, 2))
print(h)
print(l)
print(e)