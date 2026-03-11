from numpy import*
v = array(eval(input("V: ")))
numeros = []
for x in v:
	if x == 9:
		numeros.append(0)
	else:
		numeros.append((x + 1) ** 2)
print("[" + " " .join(map(str, numeros)) +"]")
		