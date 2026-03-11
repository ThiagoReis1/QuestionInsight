t= input("(T/P): ")

if t.upper() == "T":
	p = int(input("quantidade de fatias de torta ou pastel: "))
	c = int(input("quantidade cappuccinos: "))
	vt = (p * 6) + (c * 4.5)
	print(vt)
			
else:
	p = int(input("quantidade de fatias de torta ou pastel: "))
	c = int(input("quantidade cappuccinos: "))
	vt = (p * 5) + (c * 4.5)
	print(vt)