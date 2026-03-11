p = input("").upper()

c= 0
v=0

while c< len(p):
	if p[c]== "M":
		v+= 7.25
	elif p[c] == "P":
		v+=4.75
	elif p[c] == "R":
		v+= 3.5
	c+=1
print(round(v,2))