x = int(input("entrada: "))

if x < 12:
	y = 1.25 + 20
elif x == 12:
	y =  2.25 + 20
else:
	y = 3.25 + 20
print(round(y, 2))