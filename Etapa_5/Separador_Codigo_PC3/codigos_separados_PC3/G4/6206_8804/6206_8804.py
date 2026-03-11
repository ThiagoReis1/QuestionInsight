n = int(input(""))

CONT = 0

while n > -1:
	if n > 0 and n < 25:
		CONT = CONT + 1
	n = int(input(""))
print(CONT)