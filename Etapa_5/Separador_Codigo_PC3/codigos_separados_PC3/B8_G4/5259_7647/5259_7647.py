vm = float(input("Valor da Mensalidade: "))
nc = int(input("Numero de Criancas: "))

if(nc==1):
	vt = (vm * nc) - (vm * 0.1)
	print(round(vt,2))
elif(nc==2):
	vt = (vm * nc) - (vm * (nc * 0.3))
	print(round(vt,2))
elif(nc>=3):
	vt = (vm * nc) - (vm * (nc * 0.4))
	print(round(vt,2))