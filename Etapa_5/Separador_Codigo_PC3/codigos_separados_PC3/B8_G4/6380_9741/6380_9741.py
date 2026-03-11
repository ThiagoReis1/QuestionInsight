from numpy import*

prod = input().upper().split(',')
v = zeros(4, dtype=int)

for i in range(0, size(prod)):
	if prod[i] == "E":
		v[0] +=1
	elif prod[i] == "V":
		v[1] +=1
	elif prod[i] == "A":
		v[2] +=1
	elif prod[i] == "D":
		v[3] +=1
		
print(v)