x = input("Unidade: ").upper()
t = 0

while (x != "S"):
	if (x == "ICOMP"):
		t = t + 1
		x = input("Unidade: ").upper()
	else:
		t = t
		x = input("Unidade: ").upper()
print(t)
	