n = input("cara ou coroa:").upper()

cont = 0 
contcr = 0

while n != "S":
	if n == "CARA":
		contcr = contcr + 1
	cont = cont + 1
	n = input("cara ou coroa:").upper()
print(contcr)