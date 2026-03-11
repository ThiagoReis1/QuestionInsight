vm = float(input("Valor da Mensalidade: "))
nc = float(input("Numero de Criancas: "))

if(nc == 1):
	vt = (vm * 0.9) * nc
	print(round(vt , 2))
elif(nc == 2):
	vt = (vm * 0.7) * nc
	print(round(vt , 2))
elif(nc >= 3):
	vt = (vm * 0.6) * nc
	print(round(vt , 2))