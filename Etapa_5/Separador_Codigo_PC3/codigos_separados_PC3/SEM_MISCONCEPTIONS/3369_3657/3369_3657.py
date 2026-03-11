unidade=input("De a unidade: ")
valor=float(input("De o valor da velocidade: "))
k= unidade=='M'
if(k):
	vkm=3.6*valor
	print(round(vkm,2))
else:
	vms=valor/3.6
	print(round(vms,2))