aprov = input("SIM ou NAO?").upper()

NAO = 0
SIM = 0

while aprov != "S":
	if aprov == "SIM":
		SIM += 1
	NAO += 1
	aprov = input("SIM ou NAO?").upper()
total = SIM 
print(total)