resp = input().upper()
c = 0
while resp != "S":
	if resp == "SIM":
		c = c + 1
	resp = input().upper()
print(c)