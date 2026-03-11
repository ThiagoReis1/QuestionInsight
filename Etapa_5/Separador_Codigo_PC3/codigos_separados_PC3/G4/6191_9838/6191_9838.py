n1 = input("moeda: ").upper()

C = 0
C1 = 0

while (n1 != "S"):
	if (n1 == "CARA"):
		C1 = C1 + 1
	n1 = input("moeda: ").upper()
	C = C + 1

print(C1)