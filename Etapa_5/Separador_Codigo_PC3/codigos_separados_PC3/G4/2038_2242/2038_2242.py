res = input(": ").upper()
num = 0
while(res != "S"):
	if(res == "SIM"):
		num = num + 1
	res = input(": ").upper()
print(num)