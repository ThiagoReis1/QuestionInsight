nome = input()
nomea = nome.lower()

#aspartato: C4H6NO4
#Cisteina: C3H7NO2S

asp = (12.011*4) + (1.00794*6) + 14.0067 + (15.9994*4)
cist = (12.011*3) + (1.00794*7) + 14.0067 + (15.9994*2) + 32.066

if (nomea == "aspartato" ):
	print(round(asp, 2))
	
else:
	print(round(cist, 2))