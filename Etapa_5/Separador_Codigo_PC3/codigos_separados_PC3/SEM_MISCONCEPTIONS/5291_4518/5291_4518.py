afir = input().upper()
acumS = 0
cont = 0

while(afir != "S"):
	if afir == "SIM":
		acumS += 1
		cont += 1
		afir = input().upper()
	
	else:
		cont += 1
		afir = input().upper()
		
print(cont)
print(round(acumS / cont, 2) * 100)