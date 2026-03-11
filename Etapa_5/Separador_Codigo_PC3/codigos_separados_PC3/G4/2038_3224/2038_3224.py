resp = input()
s = 0

if(resp != "S"):
	while(resp != "S"):
		if(resp == "SIM"):
			s = s + 1
		resp = input()
print(s)