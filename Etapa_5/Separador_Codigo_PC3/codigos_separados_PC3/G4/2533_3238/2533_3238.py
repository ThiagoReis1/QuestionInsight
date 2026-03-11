Vi = float(input("Valor total: "))
C = float(input("Valor retirado: "))
J = float(input("Juros: "))
j = J / 100
m = 0 
v = Vi
c = C

if ((Vi > 0) and (C > 0) and (j > 0)):
	while (v <= (Vi / 2)):
		v = v + (v * j) - c
		m = m + 1
	print(round(m,2))