pc = float(input(""))
if (pc <= 50):
	vf = pc + (100 / 100 * pc)
elif (pc >= 50.01) and (pc <= 100):
	vf = pc + (50 / 100 * pc)
elif (pc >= 100.01) and (pc <= 500):
	vf = pc + (40 / 100 * pc)
else:
	vf = pc + (30 / 100 * pc)
print(round(vf,2))