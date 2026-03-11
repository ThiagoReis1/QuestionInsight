x = input("Cor da casa: ")
x = x.upper()
if (x == "PRETA"):
	p=1
else:
	p=0
while (x != "S"):
	x = input("Cor da casa: ")
	x = x.upper()
	if (x == "PRETA"):
		p = p  + 1
print(p)