def gas(l):
	if l < 17.5:
		l += 1.5
		print(round(l,1))
	elif l > 17.5 and l < 35.0:
		l += 2.3
		print(round(l,1))
	elif l >= 50:
		l += 4.7
		print(round(l,1))
	else:
		l += 3.3
		print(round(l,1))
		
gas(float(input()))