n = int(input(""))

total = 0

while n != -1:
	if (n >= 51) and (n <= 75):
		total = total + 1
		
	n = int(input(""))
	
print(total)