#ENTRADA DE DADOS
x = float (input("area: "))
#CALCULO AREA
if (x>=0) and (x<=10000) :
	v1 = (x)*(6)+(100)
	print (round(v1,2))
elif (x>10000) and (x<=20000) :
	v2 = (x)*(5.5)+(150)
	print (round(v2,2))
elif (x>20000) and (x<=30000) :
	v3 = (x)*(5)+(200)
	print (round(v3,2))
elif (x>30000) :
	v4 = (x)*(4.5)+(250)
	print (round(v4,2))