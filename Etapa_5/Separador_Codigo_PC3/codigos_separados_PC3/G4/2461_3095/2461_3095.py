pc = float(input())
if (pc <= 50):
	p2 = 2 * pc
elif(50.01 <= pc <= 100):
	p2 = pc + (pc / 2)
elif(100.01 <= pc <= 500):
	p2 = pc + (pc * 0.4)
else:
	p2 = pc + (pc * 0.3)
pf = round(p2, 2)
print(pf)