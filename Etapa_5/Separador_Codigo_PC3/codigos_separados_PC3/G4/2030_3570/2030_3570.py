face = input("cara ou coroa:")
cara = 0
f = face.upper()
if(f == "CARA") or (f == "COROA"):
	while(f != "S"):
		if(f == "CARA"):
			cara = cara + 1
			face = input("cara ou coroa:")
			f = face.upper()
		else:
			face = input("cara ou coroa:")
			f = face.upper()
print(cara)			