lp = input("L ou P:")
qntd = float(input("quantos:"))
refri = float(input("quantos refri:"))

if (lp.upper() == 'L'):
	cal = qntd*6 + refri*3
	print(round(cal,1))
	
if (lp.upper() == 'P'):
	cal = qntd*4.5 + refri*3
	print(round(cal,1))