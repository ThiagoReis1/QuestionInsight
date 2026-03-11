x = float(input("quant de horas trabalhadas: "))
if x<=20:
	res = 50*x
	print(round(res,2))
else:
	res = (50*20)+70*(x-20)
	print(round(res,2))