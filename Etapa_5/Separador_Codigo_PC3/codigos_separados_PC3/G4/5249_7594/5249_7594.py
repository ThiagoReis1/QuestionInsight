p = int(input())
s = int(input())
b = int(input())


if p == 1:
	pc = 180
elif p == 2:
	pc = 230
elif p == 3:
	pc = 250
elif p == 4:
	pc = 350
else:
	pc = 0
	
if s == 1:
	sc = 75
elif s == 2:
	sc = 110
elif s == 3:
	sc = 170
elif s == 4:
	sc = 200
else:
	sc = 0

if b == 1:
	bc = 20
elif b == 2:
	bc = 70
elif b == 3:
	bc = 100
elif b == 4:
	bc = 65
else:
	bc = 0
	
if (pc or sc or bc) == 0:
	print("Dados invalidos")
else:
	print("Calorias:",  pc+sc+bc, "cal")