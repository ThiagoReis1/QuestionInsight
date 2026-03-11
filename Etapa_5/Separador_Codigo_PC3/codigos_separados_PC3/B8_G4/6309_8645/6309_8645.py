v = input("v: ")


i = 0
h = 0
h1 = 0
c = 0
c1 = 0
l = 0
l1 = 0
while i < len(v):
	if v[i] == "H":
		h = h + 5.40
		i = i + 1
		h1 = h1 + 1
	elif v[i] == "C":
		c = c + 8.95
		i = i + 1
		c1 = c1 + 1
	elif v[i] == "L":
		l = l + 4.50
		i = i + 1
		l1 = l1 + 1
		
t = h + c + l 
t1 = round(t, 2)
print(t1,h1,c1,l1)
		