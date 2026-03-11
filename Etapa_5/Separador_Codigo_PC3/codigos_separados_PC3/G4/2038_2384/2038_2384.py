r = input()
n = 0

while(r.upper() != "S"):
	while(r.upper() == "SIM"):
		n = n + 1
		r = input()
	while(r.upper() == "NAO"):
		r = input()
print(n)
	

	