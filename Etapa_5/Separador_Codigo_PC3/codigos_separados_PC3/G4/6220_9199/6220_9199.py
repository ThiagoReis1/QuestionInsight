x = int(input("digite:"))
y = int(input("digite:"))
acum = 0

while (x <= y):
	if x%3 == 0:
		acum = acum + x
	x += 1
print(acum)	