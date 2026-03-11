x = float(input("notas: "))
y = float(input("notas: "))
z = float(input("notas: "))

me = 3
mf = (x+y+z) / me

print(round(mf, 2))


if mf >= 6:
	print("Aprovacao")
else:
	print("Reprovacao")


