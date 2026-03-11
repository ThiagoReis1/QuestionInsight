dias = int(input("Dias reservados: "))
cd = 175

if dias < 15:
	tot=(cd*dias)+20
elif dias == 15:
	tot = (cd*dias)+16
else:
	tot = (cd*dias)+10
	
print(round(tot,3))
