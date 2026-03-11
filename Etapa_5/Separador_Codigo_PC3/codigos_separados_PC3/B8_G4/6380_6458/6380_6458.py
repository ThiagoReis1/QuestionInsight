from numpy import*

c = input("qual a sequencia: ").upper().split(",")

v = zeros(4,dtype=int)

for i in range(size(c)):
	if c[i] =="E":
		v[0]+=1
	elif c[i] =="V":
		v[1]+=1
	elif c[i] == "A":
		v[2]+=1
	elif c[i] == "D":
		v[3]+=1
print(v)