vd = int(input("Digite a quantidade de duplhas: "))
dp = 32.90
vd1 = vd * dp

if vd > 3:
	vd2 = vd1 * 20/100
	print(round(vd1 - vd2, 2))
	
else:
	print(round(vd1, 2))