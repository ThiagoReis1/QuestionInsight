bc = input("fatia de bolo ou croissant? B/C: ")
qbc = int(input("quantidade de fatias de bolo ou croissant: "))
qcap = int(input("quantidade de cappuccinos: "))

fb = 3.00
c = 6.00
cap = 5.50

t1 = (fb * qbc) + (cap * qcap)
t2 = (c * qbc) + (cap * qcap)

if (bc == 'B'):
	print(round(t1, 2))
	
else:
	print(round(t2, 2))