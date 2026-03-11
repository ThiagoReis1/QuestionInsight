t_ou_p = input("torta ou pastel: ")
quant_f_P = float(input("quantidade: "))
quant_capp = float(input("quantidade: "))

fatia_de_torta = 6.00
pastel = 5.00
cappu = 4.50


if  t_ou_p == "T":
	total = quant_f_P * fatia_de_torta + quant_capp * cappu
else: 
	total = quant_f_P * pastel + quant_capp * cappu
print(round(total,2))