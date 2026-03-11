giro = input("Em que cor a bolinha caiu? ").upper()

cont = 0
acpreta = 0

while(giro != "S"):
	if(giro == "PRETA"):
		acpreta = acpreta + 1
	giro = input("Em que cor a bolinha caiu? ").upper()
	cont = cont +1
	porcp = (acpreta/cont)*100
print(cont)
print(round(porcp, 2))