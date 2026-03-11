r = input().upper()
if r == ("SIM"):
	sim = 1
else:
	sim = 0
	while (r != "S"):
		r = input().upper()
		if r == ("SIM"):
			sim = sim + 1
print(sim)