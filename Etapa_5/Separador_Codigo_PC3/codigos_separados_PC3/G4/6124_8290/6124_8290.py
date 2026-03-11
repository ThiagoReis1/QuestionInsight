pt = float(input('peso tripulante: '))

#z * pt = round(tz, 1)
#not(pt < 3000) or (pt > 4500)

if (pt < 3000) or (pt > 4500):
	tz = 'entrada invalida'
	
elif (pt >= 3000) and (pt < 3400):
	tz = pt * 0.8
	
elif (pt >= 3400) and (pt < 3900):
	tz = pt * 1.3
	
elif (pt >= 3900) and (pt < 4100):
	tz = pt * 2.1
	
else:
	tz = pt * 3
	
print(round(tz, 1))
	