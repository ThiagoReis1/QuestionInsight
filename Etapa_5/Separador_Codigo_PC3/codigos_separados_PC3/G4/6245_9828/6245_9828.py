o = input("O: ").upper()
c = 0

while o != "X":
	if o == "S":
		c = c + 1
	o = input("O: ").upper()
	
print(c)	