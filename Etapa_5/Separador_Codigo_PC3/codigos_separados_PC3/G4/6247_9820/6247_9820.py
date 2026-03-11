var = input('ICE, FT, ICOMP').upper()

ft = 0

while (var != 'X'):
	if (var == 'FT'):
		ft += 1
	var = input('ICE, FT, ICOMP').upper()
print(ft)
