#Gabriel Felipe
#19/07/16

x = float(input("abs : "))
y = float(input("coor: "))

if(x>0 and y>0):
	qua = "no quadrante 1"	
	print("O ponto (",x,",",y,") estah",qua)	
	
elif(x<0 and y>0):	
	qua = "no quadrante 2"	
	print("O ponto (",x,",",y,") estah",qua)
	
elif(x<0 and y<0):
	qua = "no quadrante 3"	
	print("O ponto (",x,",",y,") estah",qua)
	
elif(x>0 and y<0):	
	qua = "no quadrante 4"	
	print("O ponto (",x,",",y,") estah",qua)
	
else:	
	qua = "situado sobre um dos eixos"	
	print("O ponto (",x,",",y,") estah",qua)	
	
	