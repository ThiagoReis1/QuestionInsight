p = input().upper()

x = 0

while p != "S":
	if p == "SIM":
		x += 1
	p = input().upper()
	
print(x)