vv= float(input("valor de vendas de um funcionarios: "))

if vv<=1000:
	vt= (vv*5)/100
	print(round(vt, 2))
	
else: 
	va= vv-1000
	vb= (va*10)/100
	vt= vb + (1000*5)/100
	print(round(vt, 2))
