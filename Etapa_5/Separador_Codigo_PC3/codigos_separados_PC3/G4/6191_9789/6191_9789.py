x = input("insira cara ou coroa: ").upper()

cara = 0

while x != "S":
	if x == "CARA":
		cara += 1 
	x = input("insira cara ou coroa: ").upper()
	

print(cara)

   