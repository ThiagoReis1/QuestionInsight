x1 = input().upper()

tt = 0

while x1 != 'X':
	if x1 == 'FT':
		tt = tt +1
		x1 = input()
	elif x1 == 'ICOMP' or x1 == 'ICE':
		x1 = input()
print(tt)