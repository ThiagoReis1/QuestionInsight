dia = int(input(''))
diaria = 100

if (dia < 7):
	taxa = 15.00
elif (dia == 7):
	taxa = 12.00
else:
	taxa = 10.00

total = (dia * diaria) + taxa

print (round(total,2))