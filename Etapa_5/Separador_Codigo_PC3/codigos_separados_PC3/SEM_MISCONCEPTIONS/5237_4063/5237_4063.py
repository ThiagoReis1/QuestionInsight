a = float(input("D: "))
b = float(input("D: "))
c = float(input("D: "))

a1 = a % 2
b1 = b % 2
c1 = c % 2
	if a1 == 0:
		if b1 == 0:
			if c1 == 0:
				print("SIM")
			elif c1 != 0:
				print("SIM")
	if b1 != 0:
		if c1 != 0:
			print("SIM")
		elif c1 != 0:
			print("NAO")
elif (a1 != 0):
	if b1 == 0:
		if c1 == 0:
			print("SIM")
		elif c1 != 0:
			print("NAO")
			if b1 != 0:
				if c1 != 0:
					print("SIM")
				elif c1 != 0:
					print("NAO")