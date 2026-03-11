a = input("(C/E): ")

if a.upper() == "C":
	b = float(input("quantidade de coxinhas: "))
	c = float(input("quantidade de sucos: "))
	
	vf = (b * 2) + (c * 6)
	print(vf)
	
else:
	b = float(input("quantidade de esfirras: "))
	c = float(input("quantidade de sucos: "))
	
	vf = (b * 4.50) + (c * 6)
	print(vf)