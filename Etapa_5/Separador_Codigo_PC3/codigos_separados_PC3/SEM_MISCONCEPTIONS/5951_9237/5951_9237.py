# T = 4.50
# S = 5.00
# A = 12.0

alter_T_S = input("T ou S: ")
quant_T_S = int(input("quantidade ts: "))
quant_Aca = int(input("quantidade ac: "))

if alter_T_S == "T":
	Valor = (quant_T_S * 4.50) + (quant_Aca * 12.00)
	print(round(Valor, 2))
	
else:
	Valor = (quant_T_S * 5.00) + (quant_Aca * 12.00)
	print(round(Valor, 2))