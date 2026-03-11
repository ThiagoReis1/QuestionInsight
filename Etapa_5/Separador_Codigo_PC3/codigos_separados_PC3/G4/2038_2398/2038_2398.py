son = input("sim ou não? ")
qs = 0

while(son.upper()!= "S"):
	if(son.upper()=="SIM"):
		qs = qs + 1
		son = input("sim ou não? ")
	else:
		son = input("sim ou não? ")
print(qs)