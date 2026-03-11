massa = float(input("Massa: "))

i = 0
y = 0

while massa > 0.5:
	massa = massa * 0.9
	
	y = y + 1

print(y)