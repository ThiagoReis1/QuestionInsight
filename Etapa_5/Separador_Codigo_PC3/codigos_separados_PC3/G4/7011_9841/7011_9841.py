x = int(input("numero [x]: "))
y = int(input("numero [y]: "))
while x < y+1:
	if x % 5 == 0:
		print(x)
	x = x + 1
