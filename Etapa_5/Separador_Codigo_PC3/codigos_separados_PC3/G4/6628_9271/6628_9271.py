s = input("Digite a string: ").upper()

a = 0

for x in s:
	if (x == "E") or (x == "e"):
		a = a + 1
print(a)