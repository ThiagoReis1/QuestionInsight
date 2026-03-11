from numpy import*

o = input("cor dos olhos: ").split(",")
v = zeros(5, dtype=int)

for i in range(size(o)):
	if o[i] == "P":
		v[0]+=1
	elif o[i] == "C":
		v[1]+=1
	elif o[i] == "M":
		v[2]+=1
	elif o[i] == "V":
		v[3]+=1
	elif o[i] == "A":
		v[4]+=1
print(max(v))
print(v)