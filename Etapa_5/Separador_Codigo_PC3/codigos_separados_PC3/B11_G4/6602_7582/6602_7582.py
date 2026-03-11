# faça seu código aqui!
n = int(input("digite "))
prato_e = input("digite prato escolhido ").upper()
c = 0
while c < n:
	if prato_e == "L":
		cont = 0
		prato_e = cont+1
	prato_e = input("digite o prato ").upper()
while c<n:
	if prato_e == "C":
		cont = 0
		prato_e = cont+1
	prato_e = input("digite prato ").upper()
	if prato_e == "P":
		cont = 0
		prato_e = cont +1
print(prato_e)