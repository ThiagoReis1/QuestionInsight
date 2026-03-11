from numpy import*

p = input("").upper().split(',')

v = zeros(5,dtype=int)

for i in range(size(p)):
	if(p[i] == "CNH"):
		v[0] = v[0]+1
	elif(p[i] == "JPN"):
		v[1] = v[1]+1
	elif(p[i] == "KOR"):
		v[2] = v[2]+1
	elif(p[i] == "MGL"):
		v[3] = v[3]+1
	elif(p[i] == "THA"):
		v[4] = v[4]+1
print(max(v))
print(v)