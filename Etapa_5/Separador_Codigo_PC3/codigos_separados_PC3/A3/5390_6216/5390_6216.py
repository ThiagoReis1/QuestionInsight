entrada = input("Rotulo da etiqueta: ").lower()
j = 0
vt = 0
vogal = ["a","e","i","o","u"]

for l in entrada:
	if l in vogal:
		vt = vt + 0.19
	else:
		vt = vt + 0.23
print(round(vt,2))		
