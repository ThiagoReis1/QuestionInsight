crg_hor = float(input("Digite o valor da carga horaria: "))

#carga horaria entre 0 e 10h
pag_1 = crg_hor * 50 + 500

#carga horaria entre 10h e 20h
pag_2 = crg_hor * 60 + 600

#carga horaria entre 20h e 30h
pag_3 = crg_hor * 70 + 700

#carga horaria meio que 30h
pag_4 = crg_hor * 80 + 800

if (crg_hor > 0 and crg_hor < 10 or crg_hor == 10):
	print(pag_1)
elif (crg_hor > 10 and crg_hor < 20 or crg_hor == 20):
		print(pag_2)
elif (crg_hor > 20 and crg_hor < 30 or crg_hor == 30):
		print(pag_3)
else:
		print(pag_4)
		

	