d = int(input("distancia da entrega (em km): "))                                           

if (d<10):                           
	tx = 5.50                                         #taxa adicional
	ct = 50.00 + tx                                      #custo total
elif (d==10):
	tx = 7.75
	ct = 50.00 + tx
else:
	tx = 10.00
	ct = 50.00 + tx
	
print("total=", round(ct,2))
