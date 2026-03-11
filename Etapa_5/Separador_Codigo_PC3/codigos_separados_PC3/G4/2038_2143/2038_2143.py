d = input("resp ").upper()

g = 0
while(d != "S"):
	if(d == "SIM"):
		g = g + 1
		d = input("resp ").upper()
	else:
		d = input("resp ").upper()
print(g)
