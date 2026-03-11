hextra = float(input("Numero de hora extra: "))
hfalta = float(input("Numero hora falta: "))

if (hextra < 0 and hfalta < 0):
	print(hextra,"horas extras e",hfaltas,"horas de falta")
	print("Dados invalidos")

indice = hextra - 2/3*hfalta

if(indice > 2400):
	print("Entradas: ",hextra,"horas extras e",hfalta,"horas de falta")
	gratificacao = 500.0
	print("Gratificacao: R$ ",round(gratificacao, 2))
elif(indice > 1800 and indice <= 2400):
	prit("Entradas: ",hextra,"horas extras e",hfalta,"horas de falta")
	gratificacao = 400.0
	print("Gratificacao:R$ ",round(gratificacao, 2))
elif(indice > 1200 and indice <= 1800):
	print("Entradas:",hextra,"horas extras e",hfalta,"horas de falta")
	gratificacao = 300.0
	print("Gratificacao: R$ ",round(gratificacao, 2))
elif(indice > 600 and indice <= 1200):
	print("Entradas:",hextra,"horas extras e",hfalta,"horas de falta")
	gratificacao = 200.0
	print(round("Gratificacao: R$ ",gratificacao, 2))
elif (indice <= 600):
	print("Entradas:",hextra,"horas extras e",hfalta,"horas de falta")
	gratificacao = 100.0
	print("Gratificacao: R$",round(gratificacao, 2))
	



