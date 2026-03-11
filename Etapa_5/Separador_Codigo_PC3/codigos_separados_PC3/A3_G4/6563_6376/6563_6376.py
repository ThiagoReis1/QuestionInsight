dr = int(input("dias reservados: "))
dia = 175
if (dr < 15):
	x = 175 * dr + 20
elif (dr == 15):
	x = 175 * dr + 16
else:
	x = 175 * dr + 10

print("total= ",round(x, 2))