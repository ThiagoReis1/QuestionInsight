resp = input("SIM ou NAO:").upper()
cont = 0
while resp != "S":
	if resp == "SIM":
		cont = cont+1
	resp = input("SIM ou NAO:").upper()
print(cont)

