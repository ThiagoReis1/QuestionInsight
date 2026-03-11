horas=float(input("Digite as horas trabalhadas:  "))
if (horas<=20):
	sal=(horas*50)
	print(round(sal, 2))
else:
	sdm=(horas-20)
	sl=(1000+(sdm*70))
	print(sl)