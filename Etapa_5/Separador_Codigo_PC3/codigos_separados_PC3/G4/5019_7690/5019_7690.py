s = float(input("Salario: "))
if ( s < 1212):
	rea = s + (s * (12/100))
	print(round(rea,2))
elif ( s <= 5000):
	rea = s + (s * (8/100))
	print(round(rea,2))
else:
	rea = s +( s * (3/100))
	print(round(rea,2))
