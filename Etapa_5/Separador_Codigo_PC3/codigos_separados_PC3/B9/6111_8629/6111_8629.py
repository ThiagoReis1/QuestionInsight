gc = float(input("gasolina comum: "))

if (gc < 17.5):
	gd = 10.5
	mistura = gc + gd 
elif ( gc >= 17.5 and gc <= 35):
	gd = 14
	mistura = gc + gd
elif (gc >= 35 and gc <= 50):
	gd = 18.6
	mistura = gc + gd
else:
	gd = 24.5
	mistura = gc + gd
	
print(round(mistura,2))