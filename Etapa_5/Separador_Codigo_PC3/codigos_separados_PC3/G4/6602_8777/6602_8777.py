N = int(input("Quantidade do grupo: "))
c = 0
cp = 0
cc = 0
cl = 0
while N > c:
	prato_escolhido = input("Prato escolhido: ").upper()
	c += 1
	if prato_escolhido == "P":
		cp += 1
	if prato_escolhido == "L":
		cl += 1
	if prato_escolhido == "C":
		cc += 1
		
print("L=", cl)
print("C=", cc)
print("P=", cp)
