from numpy import*
x = input("x: ")
x = x.split(',')
v = zeros(5, dtype = int)
for i in x:
	y = max(x)
	if(x == "P"):
		v[0] = v[0] + 1
	elif(x == "C"):
		v[1] = v[1] + 1
	elif(x == "R"):
		v[2] = v[2] + 1
	elif(x == "L"):
		v[3] = v[3] + 1
	elif(x == "B"):
		v[4] = v[4] + 1
print(y)
print(v)