sat = input("Satisfeito? ").upper()

if(sat == "SIM"):
	i = 1
	
else:
	i = 0

if (sat != "S"):
	while(sat != "S"):
		sat = input("Satisfeito? ").upper()
		if(sat == "SIM"):
			i = i + 1
			
	print(i)