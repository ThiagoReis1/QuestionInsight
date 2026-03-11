pes = int(input("qual sua opniao: "))
x = SIM
y = NAO
z = S
while pes != z:
	a = x+1
	b = y+1
	c = (a / (a+b))*100
	print(round(c, 2))
	pes = input("qual sua opniao: ")