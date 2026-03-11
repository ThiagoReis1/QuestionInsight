he = float(input("Numero de Horas extras: "))
hf = float(input("Numero de Horas que faltou: "))
print("Entradas:", he, "horas extras", "e", hf, "horas de falta" )
H = ((round(he,2) - (2/3)) *round(hf,1))
print(H)
if(he>=0) or (he>=0):		  
	if(H > 2400):
		print("Gratificacao: R$ 500")
	elif(1800 < H <= 2400):
		print("Gratificacao: R$ 400")
	elif(1200 < H <= 1800):
		print("Gratificacao: R$ 300")
	elif(600 < H <= 1200):
		print("Gratificacao: R$ 200")
	elif(H<=600):
		print("Gratificacao: R$ 100")
else:
	print("Dados invalidos")		  
		