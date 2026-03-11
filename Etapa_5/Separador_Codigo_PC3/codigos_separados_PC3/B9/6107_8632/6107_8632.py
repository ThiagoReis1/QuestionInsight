CC = float(input("cc: "))

if CC < 17.5:
	total = CC + 1.5
elif CC >= 17.5 and CC <= 35:
	total = CC + 2.3
elif CC > 35 and CC <= 50:
	total = CC + 3.3
else:
	total = CC + 4.7
print(round(total, 1))