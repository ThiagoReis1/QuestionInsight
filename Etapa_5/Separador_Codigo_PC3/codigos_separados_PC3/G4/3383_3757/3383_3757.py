l=input("Libras: ")
y=float(input("Quilogramas: "))
if(l=="L"):
	x=y/2.20462
else:
	x=y*2.20462
print(round(x, 2))