con = float(input("consumo: "))
limite= 100

if(con<=limite):
	valorconta= 1.20*con
	
else:
	valorconta= ((25) + (1.40 * con))
	
print (round(valorconta,2))