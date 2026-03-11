r = " "
s = 0

while ( r != "S") :
	r = input("SIM ou NAO: ").upper()
	if ( r == "SIM") :
		s += 1
	elif ( r != "SIM" and r != "NAO" and r != "S" ):
		print("Bah")
		r = "S"

print(s)