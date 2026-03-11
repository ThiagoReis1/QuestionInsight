p = input("digite:")

c = 0 
v = 0 

while c < len(p):
	if p[c] == "B":
		v+=3.75
	elif p[c] =="C":
		v+=7.9
	elif p[c] == "E":
		v+=9.85
	c+=1
print(round(v, 2))