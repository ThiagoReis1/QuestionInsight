vel = int(input())

if	vel < 50:
	total = 60 + 4.5
	print(round(total,2))
elif	vel == 50:
	total = 60 + 5.50
	print(round(total,2))
else:
	total = 60 + 6.5
	print(round(total,2))