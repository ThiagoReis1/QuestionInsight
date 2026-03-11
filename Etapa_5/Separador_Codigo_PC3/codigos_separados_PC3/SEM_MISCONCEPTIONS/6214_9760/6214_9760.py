x = int(input("n: "))
contadora = 0

while x != -1:
	if 45 < x and x <= 150:
		contadora = contadora + 1
	x = int(input("n: "))

print(contadora)