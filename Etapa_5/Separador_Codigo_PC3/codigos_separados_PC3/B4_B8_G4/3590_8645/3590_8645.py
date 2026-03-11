from numpy import*

v=array(eval(input("v: ")))

p=0
i=0

while i < size(v):
	if v[i] == 1:
		p = p + 10
		i = i + 1
	elif v[i] == 2:
		p = p + 5
		i = i + 1
	elif v[i] == 3:
		p = p + 0
		i = i + 1
	elif v[i] == 4:	
		p = p + 5
		i = i + 1
	elif v[i] == 5:
		p = p + 20
		i = i + 1
	elif b[i] == 6:
		p = p + 10
		i = i + 1
print(p)