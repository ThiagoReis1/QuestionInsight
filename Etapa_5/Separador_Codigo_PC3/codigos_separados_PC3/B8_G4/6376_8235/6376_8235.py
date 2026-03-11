from numpy import* 

p = input("sequencia: ").upper().split(",")
v = zeros(4,dtype=int)

for i in p:
	if i == "A":
		v[0] += 1
	elif i == "B":
		v[1] += 1
	elif i == "C":
		v[2] += 1
	elif i == "D":
		v[3] += 1
		
print(v)
		
