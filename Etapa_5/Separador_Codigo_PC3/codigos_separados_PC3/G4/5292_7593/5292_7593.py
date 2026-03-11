cA = input("PRETA: ").upper()

x=0
v=0

while(cA != "S"):
	if(cA == "PRETA"):
		x = x + 1

	cA = input("PRETA: ").upper()
	v = v + 1
print(v)
print(round(x/v*100,2))

