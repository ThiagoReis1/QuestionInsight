
p = input().upper()
v = 0 
vg = "A","E","I","O","U"

for i in p:
	if i in vg:
		v += 3.15
	else:
		v += 4.17

print(round(v,2))


	
	



 