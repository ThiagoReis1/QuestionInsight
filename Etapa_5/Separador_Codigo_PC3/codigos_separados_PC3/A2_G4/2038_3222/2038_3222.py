r = input("Resposta: ").upper()
x = 0

while (r != "S"):
	if (r == "SIM"):
		x = x + 1
	else:
		x = x
	r = input("Resposta: ").upper()
print(x)
