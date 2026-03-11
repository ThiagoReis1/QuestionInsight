qi = int(input("quantidade inicial de grifos:"))
qx = int (input("novos grifos:"))
qy = int(input("grifos contaminados:"))
tt = qi + qx
t = 1
while(tt > qy ):
	qi = tt - qy
	tt = qi + qx
	t = t +1
print(t)