vm= float(input("Valor da mensalidade: "))
nc= int(input("Numero de criancas: "))

if nc==1:
	v= (vm*10)/100
	vt= vm-v
	print(round(vt, 2))
elif nc==2:
	v= (vm*30)/100
	vt= (vm-v)*2
	print(round(vt, 2))
elif nc>=3:
	v= (vm*40)/100
	vt= (vm-v)*nc
	print(round(vt, 2))
	