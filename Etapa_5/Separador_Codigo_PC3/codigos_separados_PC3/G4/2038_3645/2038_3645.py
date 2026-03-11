r = input("Sim ou Nao?: ").upper()
x = 0 #sim
while r != 'S':
	r = input("sim ou nao: ").upper()
	if r == 'SIM':
		x += 1
print(x)