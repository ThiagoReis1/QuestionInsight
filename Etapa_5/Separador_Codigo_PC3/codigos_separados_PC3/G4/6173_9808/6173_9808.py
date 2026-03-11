resp = input ("SIM ou NAO: ").upper()

cont = 0

while resp != "S":
	if resp == "SIM":
		cont+=1
	resp = input ("SIM ou NAO")

print (cont)