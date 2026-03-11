a  = input("")
a.upper()
acm = 0
while (a != "S" ):
	if(a == "SIM"):
		acm = acm + 1
	a = input("")
	a = a.upper()
print(acm)