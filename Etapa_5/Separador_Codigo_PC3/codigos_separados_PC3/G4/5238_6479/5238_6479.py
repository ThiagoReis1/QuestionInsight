a = int(input("Numero x: "))
b = int(input("Numero y: "))
c = int(input("Numero z: "))

if ((a >= 1000) and (b >= 1000) and (c >= 1000)) or ((a >= 1000) and (b >= 1000)) or ((a >= 1000) and (c >= 1000)) or ((b >= 1000) and (c >= 1000)):
	print("SIM")
	
	
else:
	print("NAO")
	