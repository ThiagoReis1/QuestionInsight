res = input("R? (V/E/D)").upper()
V = 0
E = 0
D = 0

while (res != "X"):
	if (res == "V"):
		V = V + 3
	elif (res == "E"):
		E = E + 2
	elif (res == "D"):
		D = D + 1
	res = input("R? (V/D/E)").upper()
print(V)
print(E)
print(D)
	
	