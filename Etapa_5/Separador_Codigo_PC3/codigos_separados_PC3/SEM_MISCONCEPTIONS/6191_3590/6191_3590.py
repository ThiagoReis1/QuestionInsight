moeda = input()

cara = 0
while(moeda != "S"):
	if(moeda.upper() == "CARA"):
		cara += 1
		
	moeda = input()
	
print(cara)