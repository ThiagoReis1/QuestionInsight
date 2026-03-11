#osenildo
n1 = float(input('Entre n1: '))
n2 = float(input('Entre n2: '))
n3 = float(input('Entre n3: '))
n4 = float(input('Entre n4: '))
n5 = float(input('Entre n5: '))
m = (n1 + n2 + n3 + n4 + n5) /5
M = round(m, 2)
if m < 7:
	print(M)
	print("Reprovacao")	
else:
	print(M)
	print("Aprovacao")
	