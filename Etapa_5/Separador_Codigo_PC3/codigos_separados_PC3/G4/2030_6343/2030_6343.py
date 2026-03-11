face = input("face: ")
acum = 0 
while (face.upper() != "S"):
	if (face.upper() == "CARA"):
	   acum = acum + 1
	face = input("face: ")
print(acum)
