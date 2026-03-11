strg = input("Digite: ").upper()
#doces = 2.25
#salgados = 4.0
#integrais = 6.90
i = 0 
total = 0
while i < len(strg):
	if strg[i] == "D":
		total = total + 2.25 
	if strg[i] == "S":
		total = total + 4.0
	if strg[i] == "I":
		total = total + 6.90
	i = i + 1

print(round(total,2))