valor= input("tapioca ou salgado? (T/S)").upper()
quant= int(input("quantidade de tapioca ou salgado:"))
qn_acai= int(input("quantidade de acai:"))

if valor == "S": 
	total = 4 * quant + 10.00 * qn_acai
	print(total)
	
else:
	total= 5.50 * quant + 10.00 * qn_acai
	print(total)
	
	

	
	