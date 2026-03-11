x = int(input(""))
cal = 0
contc = 0
conttotal = 0
zero = 0
while (x != (-1)):
	x = int(input(""))
	if (x == 5):
		contc += 1
	else:
		zero += 0
	conttotal += 1
cal = cal + ((contc * 100)/ conttotal)
print(conttotal)
print(round(cal,2))