r = str(input("o atendimento foi satisfatorio SIM ou NAO: "))
resp = str(r.upper())
cont = 0
contN = 0
while(resp!="S"):
	if(resp == "SIM"):
		cont = cont + 1
	else:
		contN = contN + 1
	r = str(input("o atendimento foi satisfatorio SIM ou NAO: "))
	resp = str(r.upper())

		
print(cont)